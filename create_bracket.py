from bracketeer import build_bracket
b = build_bracket(
        outputPath='output.png',
        teamsPath='Teams.csv',
        seedsPath='TourneySeeds.csv',
        submissionPath='submissions/XGBoost.csv',
        slotsPath='TourneySlots.csv',
        year=2019
)
