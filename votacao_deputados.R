library(dplyr)

deputados <- read.csv("~/Documents/ad2/previsaoImpeachment/dados_deputados/deputados.csv", sep=";",encoding = "utf-8",check.names = T)
summary(deputados)
deputados <- deputados %>% arrange(nome) %>% droplevels()

deputados$nome <- gsub("[^[:alnum:] ]", "", deputados$nome)
unique(deputados$nome)

imp.votacao <- read.csv("~/Documents/ad2/previsaoImpeachment/dados_deputados/imp-votacao.csv",encoding = "utf-8", check.names = T)
imp.votacao <- imp.votacao %>% select(deputado, voto)
colnames(imp.votacao) <- c("deputado", "IMPEACHMENT")
summary(imp.votacao$deputado)

unwanted_array = list(    'Š'='S', 'š'='s', 'Ž'='Z', 'ž'='z', 'À'='A', 'Á'='A', 'Â'='A', 'Ã'='A', 'Ä'='A', 'Å'='A', 'Æ'='A', 'Ç'='C', 'È'='E', 'É'='E',
                          'Ê'='E', 'Ë'='E', 'Ì'='I', 'Í'='I', 'Î'='I', 'Ï'='I', 'Ñ'='N', 'Ò'='O', 'Ó'='O', 'Ô'='O', 'Õ'='O', 'Ö'='O', 'Ø'='O', 'Ù'='U',
                          'Ú'='U', 'Û'='U', 'Ü'='U', 'Ý'='Y', 'Þ'='B', 'ß'='Ss', 'à'='a', 'á'='a', 'â'='a', 'ã'='a', 'ä'='a', 'å'='a', 'æ'='a', 'ç'='c',
                          'è'='e', 'é'='e', 'ê'='e', 'ë'='e', 'ì'='i', 'í'='i', 'î'='i', 'ï'='i', 'ð'='o', 'ñ'='n', 'ò'='o', 'ó'='o', 'ô'='o', 'õ'='o',
                          'ö'='o', 'ø'='o', 'ù'='u', 'ú'='u', 'û'='u', 'ý'='y', 'ý'='y', 'þ'='b', 'ÿ'='y', '~'='')



imp.votacao$nome <- gsub(" ", "", imp.votacao$deputado)
imp.votacao <- imp.votacao %>% arrange(nome)
imp.votacao <- imp.votacao[2:nrow(imp.votacao),]
unique(imp.votacao$nome)

imp.votacao$nome <- chartr(paste(names(unwanted_array), collapse=''),
                           paste(unwanted_array, collapse=''),
                           imp.votacao$nome)



df_f <- merge(deputados, imp.votacao, by="nome", all.x = T)



df_f <- df_f[c("id_dep", "nome", "deputado", "partido", "UF","tema_1","tema_2","tema_3",
               "tema_4","tema_5","tema_6","tema_7","tema_8","tema_9","tema_10","tema_11",
               "tema_12","tema_13","tema_14","tema_15","tema_16","tema_17","tema_18","tema_19",
               "IMPEACHMENT")]

write.table(df_f, "deputados_temas_e_impeachment.csv", quote = FALSE, sep = ";",row.names = F,fileEncoding = "utf-8")
