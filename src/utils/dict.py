def filterOutDictNoneValues(dictToFilter):
    filtered = {k: v for k, v in dictToFilter.items() if v is not None}
    return filtered