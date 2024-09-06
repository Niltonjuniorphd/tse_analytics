SELECT count(*) AS total,
       count(DISTINCT sq_candidato) AS total_candidatos
         

FROM tb_candidaturas

--conta as linhas da atual tabela e compara com o 
--número distinto de candidatos -> se igual, os 
--candidatos são únicos e não se repetem em nenhuma linha