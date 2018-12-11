import pytest
from pymodm import MongoModel, fields, EmbeddedMongoModel
from pymodm.connection import _get_db

from newsgac.common.fields import ObjectField
from newsgac.common.mixins import CreatedUpdated, DeleteObjectsMixin

@pytest.fixture(autouse=True)
def setup_db(db):
    # drops whole db
    for collection_name in db.collection_names():
        db[collection_name].drop()


class EmbeddedModelWithObjectField(EmbeddedMongoModel):
    data = ObjectField()


class ModelWithObjectField(CreatedUpdated, DeleteObjectsMixin, MongoModel):
    data = ObjectField()
    embed = fields.EmbeddedDocumentField(EmbeddedModelWithObjectField)
    created = fields.DateTimeField()
    updated = fields.DateTimeField()


def test_delete_objects():
    m = ModelWithObjectField()
    m.data = "some object"
    m.embed = EmbeddedModelWithObjectField(data="some embedded object")
    m.save()
    db = _get_db()
    assert db['fs.files'].count() == 2
    assert db['fs.chunks'].count() == 2
    assert ModelWithObjectField.objects.count() == 1
    m.delete()
    assert db['fs.files'].count() == 0
    assert db['fs.chunks'].count() == 0
    assert ModelWithObjectField.objects.count() == 0


def test_objects_are_cleaned_up_when_saved():
    m = ModelWithObjectField()
    m.data = "some object"
    m.embed = EmbeddedModelWithObjectField(data="some embedded object")
    m.save()
    db = _get_db()
    assert db['fs.files'].count() == 2
    assert db['fs.chunks'].count() == 2
    assert ModelWithObjectField.objects.count() == 1
    m.save()
    assert db['fs.files'].count() == 2
    assert db['fs.chunks'].count() == 2
    assert ModelWithObjectField.objects.count() == 1


def test_objects_are_not_cloned_up_when_model_gets_serialized():
    m = ModelWithObjectField()
    m.data = "some object"
    m.embed = EmbeddedModelWithObjectField(data="some embedded object")
    m.embed.data = "asdasd"
    m.save()
    m.data = "some object2"
    m.embed.data = "asdasd"
    m.save()
    m.save()
    m.embed.data = "asdasd"
    m.to_son()
    m.data = "some object3"
    m.to_son()
    m.embed.data = "asdasd1"
    m.save()
    m.delete()
    db = _get_db()
    assert 0 == db['fs.files'].count()
    assert 0 == db['fs.chunks'].count()
    assert 0 == ModelWithObjectField.objects.count()