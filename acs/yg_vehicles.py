global:
    seperator: ","
    name: acs
    use_schema: True
    source : "data/acs/<sumlevel>_<tbl>_<column>.json"
    filetype: json
    source_vars:
        year: [2013]
        sumlevel: ["state", "county"]
        tbl: ["B08014"]
        column:
          start: 2
          end: 6
          zfill: 3

    preprocess:
      func: "src.plugins.preprocess.acs_preprocess"

    output : "data/output/acs/<sumlevel>_<tbl>_<column>"

    web_paths: "http://api.census.gov/data/<year>/acs5?get=GEOID,<tbl>_<column>E,<tbl>_<column>M&for=<sumlevel>&key=$ACS_KEY"
    concat: YES

    import_to_db: True
    db_settings:
        user: postgres
        password_env_var: DATAUSA_PW
        host: 162.209.124.219
        db_name: datausa

    transform:
      - type: drop
        strict: NO
        column: [tbl, sumlevel, column, state, county]

    rename:
      GEOID: geo

tables:
  "yg_vehicles":
    pk: ["year", "geo"]
    agg: sum
