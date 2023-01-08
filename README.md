<h1>Opetussovellus</h1>


<h3>Luodut toiminnallisuudet:</h3>
<li>Sisäänkirjautuminen.</li>
<li>Käyttäjän luominen.</li>
<li>Kaikkien kurssien näkeminen listana.</li>
<li>Linkki kurssisivulle kurssilistauksessa.</li>
<li>Uuden kurssin luominen admin käyttäjänä.</li>
<li>Kurssisivulla joko kurssin sivu tai linkki osallistua kurssille.</li>
<li>answers, choice_correct_answers, choice_student_answers, choices, course_text, courses, students_in_course, tasks users sql taulut.</li>
<li>Admin oikeuksien tarkastus ja toimivuus.</li>
<li>Admin (opettaja) pystyy muokkaamaan kurssia: lisäämään tekstitehtäviä, tekstimateriaalia ja monivalintakysymyksiä.</li>
<li>Opiskelija näkee tilaston omista ratkotuista tehtävistä.</li>
<li>Kysymyssivusto, josta opiskelija näkee tehtävän kysymyksen tai oman vastauksensa tehtävään. Jos oli monivalintakysymys, opiskelija näkee, oliko hänen vastauksensa oikea vai väärä.</li>
<li>Opettaja näkee kurssille osallistuvien opiskelijoiden nimet.</li>
<li>Opettaja näkee kuka on vastannut ja mitä, jokaiseen kysymykseen.</li>
<li>Opettaja voi poistaa kurssin.</li>
 

<h3>Tulevaisuudessa luotavia toiminnallisuuksia:</h3>
<li>Opettaja pystyy näkemään kussin tilastot, keitä kurssilla on ja mitä tehtäviä ovat ratkoneet.</li>
<li>Opiskelijalle lasketaan pisteitä ratkotuista tehtävistä. Monivalintakysymyksistä saa automaattisesti 1 tai 0 pistettä.</li>
<li>Opettaja voi arvostella opiskelijan tekstitehtävävastaukset ja antaa niistä piteitä.</li>
<li>Opiskelija näkee omalla sivullaan/kurssisivulla pistemääränsä jokaiseen kurssiin.</li>
<li>Virheilmoitukset näkyvät suoraan samalla sivulla (osittain jo nyt sovelluksessa).</li>
<li>Varmista, että sivuille ei pääse, jos ei ole oikeuksia/ei ole kirjautunut sisään.</li>
<li>Oikea monivalintatehtävän vastaus tulee näkyviin, heti kun opiskelija on vastannut tehtävään.</li>


<h3>Virheitä, joita korjattava:</h3>
<li>Virheilmoitusten näkyminen samalla sivulla ei toimi kaikissa tilanteissa.</li>
<li>Sovellus siirretty Herokusta Fly.io sivustolle, jonka johdosta sovelluksen kaikki toiminnit eivät toimi vielä.<li>


<h3>Sovelluksen testaaminen</h3>
<li>Sovellus siirretty Herokusta Fly.io sivustolle, jonka johdosta sovelluksen kaikki toiminnit eivät toimi vielä.</li>
<li>Sovellus on sivustolla https://opetus-sovellus.fly.dev/</li>
<li>Kun luo uuden käyttäjä, admin-arvoksi tulee False.
<li>Halutessasi testata admin-oikeuksia, käytä valmiiksi luotua admin-käyttäjää: käyttäjänimi: user1, salasana: user1. </li>
<li>Testataksesi peruskäyttäjän toiminnallisuuksia, voit luoda uuden käyttäjän sign up sivulla. Mikäli et halua luoda uutta käyttäjää, valmis peruskäyttäjä on: käyttäjätunnus: user ja salasana: user</li>
<li>Kirjautuessa sisään pääset etusivulle. Jokaisen sivun yläreunassa on linkit "List of all courses" josta pääset kurssilistaukseen, "Log out" josta voit kirjautua ulos ja "Own Page", josta voit mennä omalla sivulle.</li>
<li>Toiminnallisuuksien näkyminen/sivuston sisältö riippuu siitä oletko admin käyttäjä vai et sekä esim. siitä oletko ilmottautunut kurssille. </li>
