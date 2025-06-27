Commit d'inistalisation vers Github -> 
	Ajout de GitHub sur le git local :
		-git remote add origin git@github.com:nightmare-noe/DEVOPS.git
		-git remote -v (vérification du bon fonctionnement de la connexion)

	Premier commit
	Synchronisation avec GitHub 
		-git branch -M main
		-git push -u origin main
	
	Ajout des classes Python
		- Création de la classe `SimpleMath` avec une méthode statique `addition(a, b)`
		- Création de la classe `TestSimpleMath` héritant de `unittest.TestCase`
