Opetussovellus

Luodut toiminnallisuudet:
- Sisäänkirjautuminen.
- Käyttäjän luominen.
- Kaikkien kurssien näkeminen listana.
- Linkki kurssisivulle kurssilistauksessa.
- Uuden kurssin luominen.
- Kurssisivulla joko kurssin sivu tai linkki osallistua kurssille.
	- Linkki osallistua kurssille ei vielä toimi.
- Users, courses ja course sql taulut.


Vielä luotavaa:
- Admin oikeuksien tarkastus ja toimivuus.
- Admin (opettaja) oikeudet omistava voi luoda tehtäviä kurssille
- Tehtävät monivalinta-(automaattisesti tarkastettavat) tai tekstitehtäviä(opettaja tarkastaa).
- Opiskelija näkee tilaston omista ratkotuista tehtävistä.
- Opettaja pystyy muokkaamaan kurssia: lisäämään tehtäviä ja tekstimateriaalia.
- Opettaja pystyy näkemään kussin tilastot, keitä kurssilla on ja mitä tehtäviä ovat ratkoneet.
- Opettaja pystyy poistamaan kurssin.

Testaaminen herokussa:
- Sovellus on osoitteessa https://opetus-sovellus.herokuapp.com/
- Tällä hetkellä kun luo käyttäjä, admin arvoksi tulee False. Kuitenkin admin oikeuksien tarkastus ei vielä toimi, eli kaiken näkee myös ei admin käyttäjä.
- Signup sivulla voi palata takaisin kirjautumissivulle "Log in" napilla.
- Kirjautuessa sisään, tulee linkit "Kurssit" josta pääset kurssilistaukseen ja "Kirjaudu ulos" josta voit kirjautua ulos.
- "Kurssit" linkin takaa näet kurssilistauksen ja "Create new course" napin. 
- "Create new course" napin takaa voit luoda uuden kurssin.
- Jos klikkaat kurssilistaussivulla kurssin nimeä, se vie kurssisivulle.
- Kurssisivulla oleva linkki "Sing up for course" ei toimi vielä.
