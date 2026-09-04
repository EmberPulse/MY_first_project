# === Stage 43: Добавь пагинацию длинных списков ===
# Project: CourseBoard
def paginate(items, page_size=20):
    """Yield chunks of items for paginated display."""
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]
