#Opetussovellus

**Luodut toiminnallisuudet:**
- Sisäänkirjautuminen.
- Käyttäjän luominen.
- Kaikkien kurssien näkeminen listana.
- Linkki kurssisivulle kurssilistauksessa.
- Uuden kurssin luominen admin käyttäjänä.
- Kurssisivulla joko kurssin sivu tai linkki osallistua kurssille.
- answers, choice_correct_answers, choice_student_answers, choices, course_text, courses, students_in_course, tasks users sql taulut.
- Admin oikeuksien tarkastus ja toimivuus.
- Admin (opettaja) pystyy muokkaamaan kurssia: lisäämään tekstitehtäviä, tekstimateriaalia ja monivalintakysymyksiä.
- Opiskelija näkee tilaston omista ratkotuista tehtävistä.
- Kysymyssivusto, josta opiskelija näkee tehtävän kysymyksen tai oman vastauksensa tehtävään. Jos oli monivalintakysymys, opiskelija näkee, oliko hänen vastauksensa oikea vai väärä.
- Opettaja näkee kurssille osallistuvien opiskelijoiden nimet.
- Opettaja näkee kuka on vastannut ja mitä, jokaiseen kysymykseen
- Opettaja voi poistaa kurssin.
 

**Muita mahdollisesti tulevaisuudessa luotavia toiminnallisuuksia:**
- Opettaja pystyy näkemään kussin tilastot, keitä kurssilla on ja mitä tehtäviä ovat ratkoneet.
- Opiskelijalle lasketaan pisteitä ratkotuista tehtävistä. Monivalintakysymyksistä saa automaattisesti 1 tai 0 pistettä.
- Opettaja voi arvostella opiskelijan tekstitehtävävastaukset ja antaa niistä piteitä.
- Opiskelija näkee omalla sivullaan/kurssisivulla pistemääränsä jokaiseen kurssiin.
- Virheilmoitukset näkyvät suoraan samalla sivulla (osittain jo nyt sovelluksessa).
- Varmista, että sivuille ei pääse, jos ei ole oikeuksia/ei ole kirjautunut sisään.
- Oikea monivalintatehtävän vastaus tulee näkyviin, heti kun opiskelija on vastannut tehtävään.


**Virheitä sovelluksessa, jotka korjattava:**
- Opettaja näkee jokaisen kysymyksen kohdalla useaan kertaa oppilaiden vastaukset.
- Virheilmoitusten näkyminen samalla sivulla ei toimi kaikissa tilanteissa


**Testaaminen herokussa:**
- Sovellus on osoitteessa https://opetus-sovellus.herokuapp.com/
- Kun luo uuden käyttäjä, admin-arvoksi tulee False.
- Halutessasi testata admin-oikeuksia, käytä valmiiksi luotua admin-käyttäjää: käyttäjänimi: user1, salasana: user1. 
- Testataksesi peruskäyttäjän toiminnallisuuksia, voit luoda uuden käyttäjän sign up sivulla. Mikäli et halua luoda uutta käyttäjää, valmis peruskäyttäjä on: käyttäjätunnus: user3 ja salasana: user3
- Kirjautuessa sisään pääset etusivulle. Jokaisen sivun yläreunassa on linkit "List of all courses" josta pääset kurssilistaukseen, "Log out" josta voit kirjautua ulos ja "Own Page", josta voit mennä omalla sivulle.
- Toiminnallisuuksien näkyminen/sivuston sisältö riippuu siitä oletko admin käyttäjä vai et sekä esim. siitä oletko ilmottautunut kurssille. 
