SELECT DISTINCT
    "DRG_Desc"
FROM {{ source('cms_source', 'cms_data') }}
ORDER BY "DRG_Desc"