        
WITH

tb_cand AS (
        SELECT 
                SQ_CANDIDATO,
                NM_CANDIDATO,
                SG_UF,
                NM_UE,
                DS_CARGO,
                SG_PARTIDO,
                DS_GENERO,
                DS_GRAU_INSTRUCAO,
                DS_COR_RACA,
                DS_OCUPACAO


        FROM tb_candidaturas
),

tb_total_bens AS (   
    SELECT SQ_CANDIDATO,
           SUM(CAST(REPLACE(VR_BEM_CANDIDATO, ',', '.') AS DECIMAL(15,2))) AS totalbens

    FROM tb_bens
    GROUP BY SQ_CANDIDATO
)

SELECT t1.*,
        COALESCE(t2.totalbens, 0) AS totalBens --atribui 0 a valores nulos

FROM tb_cand as t1
LEFT JOIN tb_total_bens as t2
ON t1.SQ_CANDIDATO = t2.SQ_CANDIDATO
WHERE t1.NM_UE = 'IPATINGA'


--LIMIT 150

