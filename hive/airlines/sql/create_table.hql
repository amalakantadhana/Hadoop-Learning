create external table landing.airlines(
airline string,
avail_seat_km_per_week string,
incidents_85_99 string,
fatal_accidents_85_99 string,
fatalities_85_99 string,
incidents_00_14 string,
fatal_accidents_00_14 string,
fatalities_00_14 string
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' STORED AS TEXTFILE location '/user/dhana/data/landing/airlines/';

create external table raw.airlines(
avail_seat_km_per_week string,
incidents_85_99 string,
fatal_accidents_85_99 string,
fatalities_85_99 string,
incidents_00_14 string,
fatal_accidents_00_14 string,
fatalities_00_14 string
) partitioned by (airline string) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' STORED AS ORC location '/user/dhana/data/raw/airlines/';