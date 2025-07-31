
  
    

  create  table "cms_data_db"."public"."distinct_drgs__dbt_tmp"
  
  
    as
  
  (
    SELECT DISTINCT
    "DRG_Desc"
FROM "cms_data_db"."public"."cms_data"
ORDER BY "DRG_Desc"
  );
  