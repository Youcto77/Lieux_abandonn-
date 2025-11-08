from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur API_Youcto ! https://lieux-abandonn.onrender.com/api/images/search "

@app.route('/api/images/search', methods=['GET'])
def get_dog_image():
    data = [
  {
    "nom": "Hôpital de Saint-Vincent",
    "ville": "Paris",
    "type": "Hôpital abandonné",
    "description": "Ancien hôpital désaffecté, souvent visité par des explorateurs urbains."
  },
  {
    "nom": "La Cité de la Muette",
    "ville": "Drancy",
    "type": "Cité abandonnée",
    "description": "Ancienne cité ouvrière transformée en camp de transit pendant la Seconde Guerre mondiale, maintenant en grande partie abandonnée."
  },
  {
    "nom": "Château de la Muette",
    "ville": "Paris",
    "type": "Château abandonné",
    "description": "Vieux château abandonné avec un riche passé historique."
  },
  {
    "nom": "Usine Renault Billancourt",
    "ville": "Boulogne-Billancourt",
    "type": "Usine abandonnée",
    "description": "Ancienne usine automobile, partiellement désaffectée et à l’abandon."
  },
  {
    "nom": "Fort de Romainville",
    "ville": "Noisy-le-Sec",
    "type": "Fort militaire abandonné",
    "description": "Ancien fort militaire désaffecté, aujourd’hui en ruines."
  },
  {
    "nom": "Hôpital Saint-Jacques",
    "ville": "Paris",
    "type": "Hôpital abandonné",
    "description": "Ancien hôpital désaffecté dans le 14ème arrondissement."
  },
  {
    "nom": "Usine de la Villette",
    "ville": "Paris",
    "type": "Usine abandonnée",
    "description": "Ancienne usine industrielle laissée à l’abandon, fréquentée par les explorateurs urbains."
  }
]

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
