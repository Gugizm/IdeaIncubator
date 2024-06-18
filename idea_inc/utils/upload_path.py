def profile_picture_upload_path(instance, filename):
    return f"users/{instance.id}/profile_img/{filename}"


def skills_icon_upload_path(instance, filename):
    return f"accounts/{instance.id}/skills/{filename}"


def post_img_upload_path(instance, filename):
    return f"posts/{instance.id}/cover_img/{filename}"
