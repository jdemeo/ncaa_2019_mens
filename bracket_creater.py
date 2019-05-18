from bracketeer import build_bracket

b = build_bracket(
        outputPath='output_LR.png',
        teamsPath='Teams.csv',
        seedsPath='NCAATourneySeeds.csv',
        submissionPath='submissions/LR.csv',
        slotsPath='NCAATourneySlots.csv',
        year=2017
)
