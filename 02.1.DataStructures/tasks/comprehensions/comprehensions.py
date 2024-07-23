import typing as tp


def get_unique_page_ids(records: list[tp.Mapping[str, tp.Any]]) -> set[int]:
    visited = set()
    for record in records:
        visited.add(record)
    return visited


def get_unique_page_ids_visited_after_ts(records: list[tp.Mapping[str, tp.Any]], ts: int) -> set[int]:
    result = set()
    for record in records:
        if record["EventTime"] > ts:
            result.add(record)
    return result


def get_unique_user_ids_visited_page_after_ts(
        records: list[tp.Mapping[str, tp.Any]],
        ts: int,
        page_id: int
        ) -> set[int]:
    result = set()
    for record in records:
        if record["EventTime"] > ts and record["UserID"] == page_id:
            result.add(record)
    return result


def get_events_by_device_type(
        records: list[tp.Mapping[str, tp.Any]],
        device_type: str
        ) -> list[tp.Mapping[str, tp.Any]]:
    result = set()
    for record in records:
        if record["DeviceType"] == device_type:
            result.add(record)
    return result


DEFAULT_REGION_ID = 100500


def get_region_ids_with_none_replaces_by_default(
        records: list[tp.Mapping[str, tp.Any]]
        ) -> list[int]:
    """
    Extract visited regions with order preservation. If region not defined, replace it by default region id
    :param records: records of hit-log
    :return: region ids
    """
    result = []
    for record in records:
        region_id = record.get(["RegionId"] , DEFAULT_REGION_ID)
        result.append(record)
    return result


def get_region_id_if_not_none(
        records: list[tp.Mapping[str, tp.Any]]
        ) -> list[int]:
    result = []
    for record in records:
        region_id = record.get("RegionID")
        if region_id is not None:
            result.append(region_id)
    return result


def get_keys_where_value_is_not_none(r: tp.Mapping[str, tp.Any]) -> list[str]:
    result = []
    for key,value in r.items():
        if value is not None:
            result.append(key)
    return result
        


def get_record_with_none_if_key_not_in_keys(
        r: tp.Mapping[str, tp.Any],
        keys: set[str]
        ) -> dict[str, tp.Any]:
    result = {}
    for key,value in r.items():
        if key in keys:
            result[key] == value
        else:
            result[key] == None
    return result

def get_record_with_key_in_keys(
        r: tp.Mapping[str, tp.Any],
        keys: set[str]
        ) -> dict[str, tp.Any]:
    records = {}
    for key , value in r.items():
        if key in keys:
            records[key] == value
    return records


def get_keys_if_key_in_keys(
        r: tp.Mapping[str, tp.Any],
        keys: set[str]
        ) -> set[str]:
    
    filtered_keys = set()
    for key in r.keys():
        if key in keys:
            filtered_keys.add(key)
    return filtered_keys
