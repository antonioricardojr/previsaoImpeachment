library(dplyr)
library(ggplot2)
library(caret)


deputados_temas_e_impeachment <- read.csv("~/Documents/ad2/previsaoImpeachment/deputados_temas_e_impeachment.csv", sep=";")


summary(deputados_temas_e_impeachment)

df <- deputados_temas_e_impeachment %>% filter(!is.na(IMPEACHMENT), IMPEACHMENT %in% c("SIM", "NAO")) %>% droplevels()

summary(df)

str(df)

df <- df %>% select(-nome, -deputado)

trainIndex <- createDataPartition(df$IMPEACHMENT, p = .75, list = FALSE, times = 1)

train <- df[trainIndex,]
test <- df[-trainIndex,]




treeModel <- train(IMPEACHMENT ~ ., data = train,method = "C5.0")

treeModel

prediction <- predict(treeModel, select(test, -IMPEACHMENT))
confusionMatrix(test$IMPEACHMENT, prediction)
