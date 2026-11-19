
from ressources.models import Categorie, Ressource

donnees = {
    "Informatique": [
        ("Introduction informatique", "Les bases de l'informatique.", "Cours", "https://www.open.edu/"),
        ("Architecture ordinateur", "Les composants informatiques.", "Document", "https://www.geeksforgeeks.org/"),
        ("Systèmes exploitation", "Découvrir Windows et Linux.", "Tutoriel", "https://ubuntu.com/tutorials"),
    ],
    "Développement Web": [
        ("HTML débutant", "Apprendre HTML.", "Cours", "https://developer.mozilla.org/fr/docs/Learn_web_development/Core/Structuring_content"),
        ("CSS débutant", "Apprendre CSS.", "Tutoriel", "https://developer.mozilla.org/fr/docs/Learn_web_development/Core/Styling_basics"),
        ("JavaScript", "Apprendre JavaScript.", "Cours", "https://developer.mozilla.org/fr/docs/Web/JavaScript"),
    ],
    "Programmation": [
        ("Python débutant", "Apprendre Python.", "Cours", "https://docs.python.org/fr/3/tutorial/"),
        ("Java débutant", "Apprendre Java.", "Tutoriel", "https://dev.java/learn/"),
        ("Langage C", "Apprendre le langage C.", "Document", "https://www.learn-c.org/"),
    ],
    "Bases de données": [
        ("SQL débutant", "Apprendre SQL.", "Cours", "https://sqlbolt.com/"),
        ("MySQL", "Découvrir MySQL.", "Tutoriel", "https://dev.mysql.com/doc/"),
        ("PostgreSQL", "Découvrir PostgreSQL.", "Document", "https://www.postgresql.org/docs/"),
    ],
    "Réseaux informatiques": [
        ("Introduction réseaux", "Les bases des réseaux.", "Cours", "https://www.cisco.com/"),
        ("TCP IP", "Les protocoles réseau.", "Document", "https://developer.mozilla.org/en-US/docs/Glossary/TCP"),
        ("Sécurité réseau", "Protéger les réseaux.", "Tutoriel", "https://www.cloudflare.com/learning/network-layer/what-is-a-computer-network/"),
    ],
    "Intelligence artificielle": [
        ("Introduction IA", "Découvrir l'intelligence artificielle.", "Cours", "https://www.ibm.com/think/topics/artificial-intelligence"),
        ("Machine Learning", "Apprentissage automatique.", "Tutoriel", "https://developers.google.com/machine-learning/crash-course"),
        ("Deep Learning", "Réseaux de neurones.", "Cours", "https://www.deeplearning.ai/"),
    ],
    "Cybersécurité": [
        ("Bases cybersécurité", "Sécurité informatique.", "Cours", "https://www.cybermalveillance.gouv.fr/"),
        ("Sécurité mots de passe", "Protéger ses comptes.", "Tutoriel", "https://www.cnil.fr/"),
        ("Sécurité Web", "Les bonnes pratiques.", "Document", "https://owasp.org/www-project-top-ten/"),
    ],
    "Développement mobile": [
        ("Android", "Développer Android.", "Cours", "https://developer.android.com/courses"),
        ("iOS", "Développement Apple.", "Tutoriel", "https://developer.apple.com/tutorials/"),
        ("Flutter", "Applications multiplateformes.", "Cours", "https://docs.flutter.dev/"),
    ],
    "Design et UX UI": [
        ("Design graphique", "Principes du design.", "Cours", "https://www.canva.com/designschool/"),
        ("UX Design", "Expérience utilisateur.", "Tutoriel", "https://www.nngroup.com/articles/definition-user-experience/"),
        ("Figma", "Conception des interfaces.", "Tutoriel", "https://help.figma.com/"),
    ],
    "Bureautique": [
        ("Excel", "Apprendre Excel.", "Cours", "https://support.microsoft.com/fr-fr/excel"),
        ("Word", "Apprendre Word.", "Tutoriel", "https://support.microsoft.com/fr-fr/word"),
        ("PowerPoint", "Créer des présentations.", "Cours", "https://support.microsoft.com/fr-fr/powerpoint"),
    ],
    "Cloud Computing": [
        ("Introduction Cloud", "Découvrir le cloud.", "Cours", "https://aws.amazon.com/what-is-cloud-computing/"),
        ("Microsoft Azure", "Découvrir Azure.", "Tutoriel", "https://learn.microsoft.com/fr-fr/azure/"),
        ("Google Cloud", "Découvrir Google Cloud.", "Cours", "https://cloud.google.com/learn"),
    ],
    "Gestion de projets": [
        ("Méthode Agile", "Gestion agile.", "Cours", "https://www.atlassian.com/agile"),
        ("Méthode Scrum", "Apprendre Scrum.", "Document", "https://scrumguides.org/"),
        ("Gestion de projet", "Organiser un projet.", "Tutoriel", "https://www.pmi.org/learning"),
    ],
}

for nom, liste in donnees.items():
    categorie, _ = Categorie.objects.get_or_create(
        nom=nom,
        defaults={"description": "Ressources pédagogiques : " + nom}
    )

    for titre, description, type_ressource, url in liste:
        Ressource.objects.get_or_create(
            titre=titre,
            defaults={
                "description": description,
                "type": type_ressource,
                "url": url,
                "categorie": categorie,
            }
        )

print("Importation terminee !")
print("Total categories :", Categorie.objects.count())
print("Total ressources :", Ressource.objects.count())
