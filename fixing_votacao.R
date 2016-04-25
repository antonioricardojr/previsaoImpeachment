library(dplyr)
deputados_temas_e_impeachment <- read.csv("~/Documents/ad2/previsaoImpeachment/deputados_temas_e_impeachment.csv", sep=";")

imp.votacao <- read.csv("~/Documents/ad2/previsaoImpeachment/dados_deputados/imp-votacao.csv")



deputados_NA <- deputados_temas_e_impeachment  %>% filter(is.na(IMPEACHMENT))

write.table(deputados_NA, "deputados_NA.csv", quote = FALSE, row.names = FALSE,sep = ";")



deputados_NA$IMPEACHMENT <- deputados_na...Sheet1$IMPEACHMENT


dep_ok <- deputados_temas_e_impeachment %>% filter(!is.na(IMPEACHMENT))

dep_ok <- rbind(dep_ok, deputados_NA)
summary(dep_ok)

deputados_temas_e_impeachment <- dep_ok

write.table(deputados_temas_e_impeachment,"deputados_temas_e_impeachment_v1.1.csv", row.names = FALSE, quote = FALSE,sep = ";",fileEncoding = "UTF-8")
