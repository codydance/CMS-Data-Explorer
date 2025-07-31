SELECT
    "DRG_Desc", 
    "Rndrng_Prvdr_City" as "city",
    "Rndrng_Prvdr_State_Abrvtn" AS "state",
    AVG("Avg_Tot_Pymt_Amt") AS "avg_charge"
FROM "cms_data_db"."public"."cms_data"
GROUP BY "Rndrng_Prvdr_State_Abrvtn", "Rndrng_Prvdr_City", "DRG_Desc"