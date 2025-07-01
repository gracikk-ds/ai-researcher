"""Lists of keywords to filter papers."""

from typing import List

PREDEFINED_KEYWORDS: List[str] = [  # noqa: WPS407
    "image editing",
    "image edit",
    "editing images",
    "editing image",
    "edit the image",
    "edit image",
    "edit an image",
    "image generation and editing",
    "image-editing",
    "editing model",
]


EXCLUDE_KEYWORDS: List[str] = [  # noqa: WPS407
    "gan",
    "gans",
    "(gans)",
    "gan-like",
    "3d",
    "4d",
    "radiance fields",
    "matting",
    "cnn",
    "harmonization",
    "video",
    "attention control",
    "inversion",
    "inverse",
    "DDIM",
    "fashion",
    "bounding box",
    "medical",
    "watermark",
    "vector",
    "drag-based",
    "drag based",
    "dragging",
    "drag",
]
