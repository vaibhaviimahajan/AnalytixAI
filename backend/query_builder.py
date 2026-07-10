def build_where_clause(category="All", payment="All"):
    conditions = []

    if category != "All":
        conditions.append(f"c.category_name = '{category}'")

    if payment != "All":
        conditions.append(f"o.payment_method = '{payment}'")

    if conditions:
        return "WHERE " + " AND ".join(conditions)

    return ""