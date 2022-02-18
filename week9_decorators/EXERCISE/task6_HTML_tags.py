def tags(tag):
    def decorator(f):
        def wrapper(*args):
            result = f(*args)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator


@tags('K')
def j_str(*args):
    return "".join(args)


print(j_str("Zdr bebce,", "kpr"))