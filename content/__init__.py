from . import main, stations, areas_and_stations, info

# Import area pages from multiple sources to combine detailed content
try:
    from . import yongin_areas_gu as gu_pages
    from . import cheoin_areas
    from . import giheung_areas
    from . import suji_areas
    # Start with district pages (3) + region pages from detailed sources
    area_pages_list = (
        gu_pages.PAGES +  # 3 district pages with detailed content
        cheoin_areas.PAGES +  # 12 Cheoin-gu region pages with detailed content
        giheung_areas.PAGES +  # 12 Giheung-gu region pages with detailed content
        suji_areas.PAGES  # 6 Suji-gu region pages with detailed content
    )

    # If we don't have enough pages, fall back to the regular areas module
    if len(area_pages_list) < 21:
        from . import areas
        area_pages_list = areas.PAGES
except (ImportError, AttributeError):
    from . import areas
    area_pages_list = areas.PAGES

PAGES = (
    [main.PAGE] +
    area_pages_list +
    stations.PAGES +
    areas_and_stations.PAGES +
    info.PAGES
)
