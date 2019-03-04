# coding=utf-8
from newsgac.data_sources.process import parse_article
import newsgac.genres as DataUtils

article_1 = """__label__NIE DATE=10/04/1985 NEWSPAPER=06De_Telegraaf PAGE=3 LENGTH=237 URLS=http://resolver.kb.nl/resolve?urn=ddd:011207010:mpeg21:a0171 Man dood na doorzagen elektrische leiding ZUID-SCHARWOUDE , vrijdag Een 49-jarige man uit Zuid- Scharwoude ( gem . Langedijk ) is gisteren om het leven gekomen toen hij per ongeluk een levensgevaarlijke elektriciteitsleiding doorzaagde ."""
article_2 = """__label__NIE Man dood na doorzagen elektrische leiding ZUID-SCHARWOUDE , vrijdag Een 49-jarige man uit Zuid- Scharwoude ( gem . Langedijk ) is gisteren om het leven gekomen toen hij per ongeluk een levensgevaarlijke elektriciteitsleiding doorzaagde ."""
article_3 = """__label__OPI DATE=01/02/1965 NEWSPAPER=05NRC_Handelsblad PAGE=7 LENGTH=4138 URLS=http://resolver.kb.nl/resolve?urn=KBNRC01:000035728:mpeg21:a0094 Wat wilt u op uw scherm zien in de Oudejaarsnacht ? ALS de NTS in de decembermaand een enquête onder het Nederlandse kijkerspubliek had gehouden onder het motto : „ Wat wilt u op uw scherm zien in de Oudejaarsnacht , '' had zeker niemand ingevuld : De Munttoren in Amsterdam , voorafgegaan door een fraai maar saai spelend cello en gitaarduo alsmede een toespraak van prof. dr. J. C. Brandt Corstius . Want op een openbaar plein komt in de Oudejaarsnacht , zelfs in Amsterdam , geen kip voorbij , hoe mooi de wijzers van de aloude klok van de Munttoren ook over elkaar vallen en hoe vriendelijk ook het carillon moge klinken . En wat de spreker betreft : daar houden de Nederlanders niet van . De toespraak vóór het slaan van de klok — dat was al zo toen nog de Avrodirecteuren over de draadloze hun impressies te beste gaven — wordt plechtig aangehoord als een laatste vermaning , waarbij het verboden is al aan de champagne kurk te morrelen . Het moet een ondankbare taak zijn om hst programma voor de jaarswisseling te n : oeten bedenken , want , eerlijk gezegd , een erg positieve suggestie voor het volgen jaar kunnen wij óók niet bijdragen , of het moest zijn om de enquête , hierboven genoemd , inderdaad eens te houden. ' Overigens heeft de televisie donderdagavond wel veel boeiends geboden . We willen het niet hebben over de klucht Drie is te Veel , waarvan de omroepster al min of meer verontschuldigend meldde dat het op veelvuldig verzoek was dat deze voorstlslling werd herhaald . Boeiend was wel de mengeling van muzikale prestaties van het Haarlemse Harteweensconcert — eigenlijk een monster-top of -flop , waarbij men zich al bij voorbaat van de instemming van het publiek had verzekerd , maar waarin wij hier en daar toch nog wel eens een flopje aantroffen . Na het vele , dat al over dit voortreffelijke initiatief is geschreven , willen wij volstaan met een complimentje voor Pim Jacobs om de sympathieke manier waarop het programma bij de jeugd inleidde en aaneenreeg . Sympathiek ook vonden wij hel optreden van Josophine Baker , al is haar repertoire niet erg aangepast aan de naoorlogse smaak en zal zij de oudere kijkers meer hebben geboeid dan de teenagers . Rest ons dan de Freedom Spectacular — een voorstelling waarmee wij een beetje zijn blijven zitten . Wij kunnen niet geloven dat dit programma met betrekking tlot het rassenvraagstuk bij de Nederlandse kijker iets veranderd zal hebben , zodat de Boodschap die als een rode draad door het grijze breisel van amusement liep , voor ons land verspild mag heten . Liet men die boodschap voor wat zij was ; dan restte een aaneenschakeling van soms matige , soms goede , soms bepaald onaanzienlijke bijdragen — een soort hartiewensconcert waarin wij weinig van onze hartewensen terug vonden . e. B. Nieuwjaar Nieuwjaarsdagavond bood ais hoogtepunt op het eerste programma een speciaal televisieoptreden in het voormalige gebouw van K. en W. in Den Haaf van de Opera van Peking . De formidabele veelzijdigheid van dit gezelschap leverde cameraregisseur Leen Tlmps uiteraard veel aantrekkelijks . Toch bevond de kijker zich voor ons gevoel te vaak op te grote afstand van het toneel om een goed overzicht te krijgen . Dat gold met name de grote dwarrelende scènes en in sterke mate het boeiende slotgevecht met de achterwaartse snoeksprongen . Overigens een bijzonder plezierig ding deze Chinese Opera ook eens niet in de zaal te zien . In de plaats van het Franse televisieprogramma Pop Art ( dat wegens tijdgebrek niet naar genoegen kon worden bewerkt en helaas moest worden uitgegesteld tot later ) zagen we een overzicht van Vara 's Magazine Uit en daar viel niet meer zo erg veel aan te beleven ; bovendien zitten we alweer zo verbluffend vertrouwd in het nieuwe jaar dat terugblikken naar wat 1964 ons bood al niet meer zo op zijn plaats is . Maar ach , het was noodzaak en in Uit kwamen best aardige zaken in onze herinnering terug . Op Nederland 1 ten slotte liet de NCRV in haar actualiteitenrubriek Attentie enkele helderzienden voornamelijk politieke voorspellingen doen . Even beetje dom gedoe en bepaald beter geschikt voor het damesblad . G. B. R ."""
article_4 = """__label__OPI Wat wilt u op uw scherm zien in de Oudejaarsnacht ? ALS de NTS in de decembermaand een enquête onder het Nederlandse kijkerspubliek had gehouden onder het motto : „ Wat wilt u op uw scherm zien in de Oudejaarsnacht , '' had zeker niemand ingevuld : De Munttoren in Amsterdam , voorafgegaan door een fraai maar saai spelend cello en gitaarduo alsmede een toespraak van prof. dr. J. C. Brandt Corstius . Want op een openbaar plein komt in de Oudejaarsnacht , zelfs in Amsterdam , geen kip voorbij , hoe mooi de wijzers van de aloude klok van de Munttoren ook over elkaar vallen en hoe vriendelijk ook het carillon moge klinken . En wat de spreker betreft : daar houden de Nederlanders niet van . De toespraak vóór het slaan van de klok — dat was al zo toen nog de Avrodirecteuren over de draadloze hun impressies te beste gaven — wordt plechtig aangehoord als een laatste vermaning , waarbij het verboden is al aan de champagne kurk te morrelen . Het moet een ondankbare taak zijn om hst programma voor de jaarswisseling te n : oeten bedenken , want , eerlijk gezegd , een erg positieve suggestie voor het volgen jaar kunnen wij óók niet bijdragen , of het moest zijn om de enquête , hierboven genoemd , inderdaad eens te houden. ' Overigens heeft de televisie donderdagavond wel veel boeiends geboden . We willen het niet hebben over de klucht Drie is te Veel , waarvan de omroepster al min of meer verontschuldigend meldde dat het op veelvuldig verzoek was dat deze voorstlslling werd herhaald . Boeiend was wel de mengeling van muzikale prestaties van het Haarlemse Harteweensconcert — eigenlijk een monster-top of -flop , waarbij men zich al bij voorbaat van de instemming van het publiek had verzekerd , maar waarin wij hier en daar toch nog wel eens een flopje aantroffen . Na het vele , dat al over dit voortreffelijke initiatief is geschreven , willen wij volstaan met een complimentje voor Pim Jacobs om de sympathieke manier waarop het programma bij de jeugd inleidde en aaneenreeg . Sympathiek ook vonden wij hel optreden van Josophine Baker , al is haar repertoire niet erg aangepast aan de naoorlogse smaak en zal zij de oudere kijkers meer hebben geboeid dan de teenagers . Rest ons dan de Freedom Spectacular — een voorstelling waarmee wij een beetje zijn blijven zitten . Wij kunnen niet geloven dat dit programma met betrekking tlot het rassenvraagstuk bij de Nederlandse kijker iets veranderd zal hebben , zodat de Boodschap die als een rode draad door het grijze breisel van amusement liep , voor ons land verspild mag heten . Liet men die boodschap voor wat zij was ; dan restte een aaneenschakeling van soms matige , soms goede , soms bepaald onaanzienlijke bijdragen — een soort hartiewensconcert waarin wij weinig van onze hartewensen terug vonden . e. B. Nieuwjaar Nieuwjaarsdagavond bood ais hoogtepunt op het eerste programma een speciaal televisieoptreden in het voormalige gebouw van K. en W. in Den Haaf van de Opera van Peking . De formidabele veelzijdigheid van dit gezelschap leverde cameraregisseur Leen Tlmps uiteraard veel aantrekkelijks . Toch bevond de kijker zich voor ons gevoel te vaak op te grote afstand van het toneel om een goed overzicht te krijgen . Dat gold met name de grote dwarrelende scènes en in sterke mate het boeiende slotgevecht met de achterwaartse snoeksprongen . Overigens een bijzonder plezierig ding deze Chinese Opera ook eens niet in de zaal te zien . In de plaats van het Franse televisieprogramma Pop Art ( dat wegens tijdgebrek niet naar genoegen kon worden bewerkt en helaas moest worden uitgegesteld tot later ) zagen we een overzicht van Vara 's Magazine Uit en daar viel niet meer zo erg veel aan te beleven ; bovendien zitten we alweer zo verbluffend vertrouwd in het nieuwe jaar dat terugblikken naar wat 1964 ons bood al niet meer zo op zijn plaats is . Maar ach , het was noodzaak en in Uit kwamen best aardige zaken in onze herinnering terug . Op Nederland 1 ten slotte liet de NCRV in haar actualiteitenrubriek Attentie enkele helderzienden voornamelijk politieke voorspellingen doen . Even beetje dom gedoe en bepaald beter geschikt voor het damesblad . G. B. R ."""

def test_parse_all_fields1(app):
    article = parse_article(article_1)
    assert article.year == 1985
    assert article.source == '06De_Telegraaf'
    assert article.page == 3
    assert article.urls[0] == 'http://resolver.kb.nl/resolve?urn=ddd:011207010:mpeg21:a0171'
    assert article.raw_text.split(' ')[0] == 'Man'
    assert article.label == DataUtils.genre_codes.index('NIE')


def test_parse_label_only1(app):
    article = parse_article(article_2)
    assert article.year is None
    assert article.source is None
    assert article.page is None
    assert len(article.urls) == 0
    assert article.raw_text.split(' ')[0] == 'Man'
    assert article.label == DataUtils.genre_codes.index('NIE')


def test_parse_all_fields2(app):
    article = parse_article(article_3)
    assert article.year == 1965
    assert article.source == '05NRC_Handelsblad'
    assert article.page == 7
    assert article.urls[0] == 'http://resolver.kb.nl/resolve?urn=KBNRC01:000035728:mpeg21:a0094'
    assert article.raw_text.split(' ')[0] == 'Wat'
    assert article.label == DataUtils.genre_codes.index('OPI')


def test_parse_label_only2(app):
    article = parse_article(article_4)
    assert article.year is None
    assert article.source is None
    assert article.page is None
    assert len(article.urls) == 0
    assert article.raw_text.split(' ')[0] == 'Wat'
    assert article.label == DataUtils.genre_codes.index('OPI')