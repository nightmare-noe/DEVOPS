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

	Integration des tests dans GitHub Actions
		- Création d’un workflow `.github/workflows/python-app.yml`
		- Exécution automatique des tests à chaque `push`
		- Résultats visibles dans l’onglet "Actions" du dépôt GitHub
	
	Ajout de la soustraction 
		- Ajout d’une méthode `soustraction(a, b)` à la classe `SimpleMath`
		- Test unitaire `test_soustraction()` ajouté dans la classe `TestSimpleMath`
		

	Ajout du lint automatique avec pylint
	- `pylint` ajouté aux dépendances (`requirements.txt`)
	- Le workflow CI exécute désormais aussi un **lint** de `simple_math.py` et `test_simple_math.py`
