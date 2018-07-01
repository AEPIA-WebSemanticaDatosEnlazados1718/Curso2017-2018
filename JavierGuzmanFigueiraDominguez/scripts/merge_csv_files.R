# Load datasets
cups <- read.csv("../data/WorldCups.csv")
matches <- read.csv("../data/WorldCupMatches.csv")
players <- read.csv("../data/WorldCupPlayers.csv")

# Remove NA's and duplicated instances
matches <- matches[is.na(matches), ]
matches <- matches[!duplicated(matches$MatchID), ]

# Merge datasets by using an outer join
cups_matches <- merge(cups, matches, by = "Year", all = TRUE)
cups_matches_players <- merge(cups_matches, players, by = "MatchID", all = TRUE)

# Store full dataset in a new csv file
write.csv(cups_matches_players, file = "../data/WorldCupData.csv")