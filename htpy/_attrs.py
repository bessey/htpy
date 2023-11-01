from ._safestring import mark_safe, to_html


# Inspired by https://www.npmjs.com/package/classnames
def class_names(value):
    if isinstance(value, list | tuple | set):
        return mark_safe(" ".join(to_html(x, quote=True) for x in value if x))

    if isinstance(value, dict):
        return mark_safe(
            " ".join(to_html(k, quote=True) for k, v in value.items() if v)
        )

    return mark_safe(to_html(value, quote=True))


def kwarg_attribute_name(name):
    # Make _hyperscript (https://hyperscript.org/) work smoothly
    if name == "_":
        return "_"

    return name.removesuffix("_").replace("_", "-")


def generate_attrs(raw_attrs):
    for key, value in raw_attrs.items():
        if key == "class":
            value = class_names(value)

        if value is False:
            continue

        elif value is not True:
            value = to_html(value, quote=True)

        yield to_html(key, quote=True), value