**Opetussovellus**

Luodut toiminnallisuudet:
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
 

Muita mahdollisesti tulevaisuudessa luotavia toiminnallisuuksia:
- Opettaja pystyy näkemään kussin tilastot, keitä kurssilla on ja mitä tehtäviä ovat ratkoneet.
- Opiskelijalle lasketaan pisteitä ratkotuista tehtävistä. Monivalintakysymyksistä saa automaattisesti 1 tai 0 pistettä.
- Opettaja voi arvostella opiskelijan teksittehtävävastaukset ja antaa niistä piteitä.
- Opiskelija näkee omalla sivullaan/kurssisivulla pistemääränsä jokaiseen kurssiin.
- Virheilmoitukset näkyvät suoraan samalla sivulla (osittain jo nyt sovelluksessa).
- Varmista, että sivuille ei pääse, jos ei ole oikeuksia/ei ole kirjautunut sisään.
- Oikea monivalintatehtävän vastaus tulee näkyviin, heti kun opiskelija on vastannut tehtävään.

Testaaminen herokussa:
- Sovellus on osoitteessa https://opetus-sovellus.herokuapp.com/
- Kun luo uuden käyttäjä, admin-arvoksi tulee False.
- Halutessasi testata admin-oikeuksia, käytä valmiiksi luotua admin-käyttäjää: käyttäjänimi: user1, salasana: user1
- Signup sivulla voit luoda uuden käyttäjän.
- Signup sivulla voi palata takaisin kirjautumissivulle "Log in" napilla.
- Kirjautuessa sisään peruskäyttäjänä tulee lista kursseista, joihin on ilmoittautunut, joissa on linkit kurssien sivuille. Lisäksi sivulla on linkit "List of all courses" josta pääset kurssilistaukseen ja "Log out" josta voit kirjautua ulos.
- "List of all courses" linkin takaa näet kurssilistauksen, "Create new course" napin, mikäli olet admin käyttäjä ja "Return to own page" napin, jostä pääset omalle sivulle. 
- "Create new course" napin takaa voi admin käyttäjä luoda uuden kurssin.
- Kun klikkaat kurssilistaussivulla kurssin nimeä:
	- jos olet peruskäyttäjä ja et ole ilmoittautunut kurssille, pääset sivulle, jossa on nappi josta voit ilmottautua kurssille.
	- jos olet ilmoittautunut kurssille, näet kurssisivun.
	- jos olet admin-käyttäjä näet kurssisivun.
- Jos olet adminkäyttäjä kurssisivulla on nappi "Modify course"
	- Napin takana voit luoda uuden tekstitehtävän tai tekstimateriaalia kurssille.
