from flask import Flask, render_template, request
from predict import predict_flood

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    values = [
        float(request.form["MonsoonIntensity"]),
        float(request.form["TopographyDrainage"]),
        float(request.form["RiverManagement"]),
        float(request.form["Deforestation"]),
        float(request.form["Urbanization"]),
        float(request.form["ClimateChange"]),
        float(request.form["DamsQuality"]),
        float(request.form["Siltation"]),
        float(request.form["AgriculturalPractices"]),
        float(request.form["Encroachments"]),
        float(request.form["IneffectiveDisasterPreparedness"]),
        float(request.form["DrainageSystems"]),
        float(request.form["CoastalVulnerability"]),
        float(request.form["Landslides"]),
        float(request.form["Watersheds"]),
        float(request.form["DeterioratingInfrastructure"]),
        float(request.form["PopulationScore"]),
        float(request.form["WetlandLoss"]),
        float(request.form["InadequatePlanning"]),
        float(request.form["PoliticalFactors"])
    ]

    probability = predict_flood(values)

    percentage = round(probability * 100, 2)

    if percentage < 35:
        risk = "LOW"
    elif percentage < 70:
        risk = "MODERATE"
    else:
        risk = "HIGH"

    return render_template(
        "index.html",
        prediction=percentage,
        risk=risk
    )


if __name__ == "__main__":
    app.run(debug=True)