


var data = {
    "dévlopper front-end": [
      { "Niveau d’études Requis": 5,
        "Description": "Le métier de dévlopper inffdnfdgfdgfdgfdgfdgfdgfdgfdgfdg.",
        "Catégorie": "Télécommunication",
        "Salairedébut": 2500, 
        "lien":"http://dfdfdsfds.com"
      }
    ],
      "cybersecuritée ingenieur": [
      { "Niveau d’études Requis": 5,
        "Description": "Le métier de cyber.... inffdnfdgfdgfdgfdgfdgfdgfdgfdgfdg.",
        "Catégorie": "Défense",
        "Salairedébut": 3000, 
        "lien":"http://dfdfdsfds.com"
      }
    ]
   
   }
  

function load() {
    var jsonData = JSON.parse(data);
    console.log(jsonData);
}

load()