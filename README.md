**Opetussovellus**

Luodut toiminnallisuudet:
- Sisäänkirjautuminen.
- Käyttäjän luominen.
- Kaikkien kurssien näkeminen listana.
- Linkki kurssisivulle kurssilistauksessa.
- Uuden kurssin luominen admin käyttäjänä.
- Kurssisivulla joko kurssin sivu tai linkki osallistua kurssille.
- users, courses, students_in_course, tasks, answers ja course_text sql taulut.
- Admin oikeuksien tarkastus ja toimivuus.
- Admin (opettaja) pystyy muokkaamaan kurssia: lisäämään tekstitehtäviä ja tekstimateriaalia.
- Opiskelija näkee tilaston omista ratkotuista tehtävistä.
- Opiskelija näkee tehdyt tehtävät ja tekemättömät tehtävä kurssisivulla.

Vielä luotavaa:
- Tehtävät monivalinta-(automaattisesti tarkastettavat).
- Opettaja pystyy näkemään kussin tilastot, keitä kurssilla on ja mitä tehtäviä ovat ratkoneet.
- Opettaja pystyy poistamaan kurssin.
- Ulkoasu.
- Kaikkien syötteiden validointi.
- Virheilmoitukset näkyvät suoraan samalla sivulla.
- Varmista, että sivuille ei pääse, jos ei ole oikeuksia/ei ole kirjautunut sisään.
- Luodessa salasanaa, pyydä kirjoittaa salasana kahdesti ja tarkasta, että ovat samat.

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
