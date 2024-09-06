        
WITH

tb_cand AS (
        SELECT 
                SQ_CANDIDATO,
                SG_UF,
                DS_CARGO,
                SG_PARTIDO,
                NM_PARTIDO,
                DT_NASCIMENTO,
                DS_GENERO,
                DS_GRAU_INSTRUCAO,
                DS_ESTADO_CIVIL,
                DS_COR_RACA,
                DS_OCUPACAO


        FROM tb_candidaturas
),

tb_total_bens AS (   
    SELECT SQ_CANDIDATO,
            SUM(CAST(REPLACE(VR_BEM_CANDIDATO, ',', '.') AS DECIMAL(15,2))) AS totalbens

    FROM tb_bens
    GROUP BY SQ_CANDIDATO
),


tb_info_completa_cand AS (
    SELECT t1.*,
            COALESCE(t2.totalbens, 0) AS totalBens --atribui 0 a valores nulos
    
    FROM tb_cand as t1
    LEFT JOIN tb_total_bens as t2
    ON t1.SQ_CANDIDATO = t2.SQ_CANDIDATO

)

SELECT 
        SG_PARTIDO,
        NM_PARTIDO,
        SUM(CASE WHEN DS_GENERO = 'FEMININO' THEN 1 ELSE 0 END) AS txFeminino,
        SUM(CASE WHEN DS_GENERO = 'MASCULINO' THEN 1 ELSE 0 END) AS txMasculino

FROM tb_info_completa_cand AS t1
GROUP BY 1,2

ORDER BY 3 DESC
    
--LIMIT 100

