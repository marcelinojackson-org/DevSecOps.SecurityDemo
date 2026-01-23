import os


def _get_depth(default=2):
    value = os.getenv("SPIDER_MAX_DEPTH", str(default)).strip()
    try:
        depth = int(value)
        if depth < 0:
            return default
        return depth
    except ValueError:
        return default


def zap_spider(zap, target):
    depth = _get_depth()
    try:
        zap.spider.set_option_max_depth(depth)
        print(f"[spider-hook] Spider max depth set to {depth}")
    except Exception as exc:
        print(f"[spider-hook] Failed to set spider max depth: {exc}")
    return zap, target


def zap_ajax_spider(zap, target, max_time):
    depth = _get_depth()
    try:
        zap.ajaxSpider.set_option_max_crawl_depth(depth)
        print(f"[spider-hook] AJAX spider max crawl depth set to {depth}")
    except Exception as exc:
        print(f"[spider-hook] Failed to set AJAX spider depth: {exc}")
    return zap, target, max_time
