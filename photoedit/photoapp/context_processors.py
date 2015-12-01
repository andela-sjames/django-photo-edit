Image_Effects = dict(

        ICON_EFFECTS = dict(
          format = "png",
          transformation = [
              dict(height=95, width=95, crop="thumb", gravity="face", radius=20),
              dict(angle=10),
          ]
      ),
        THUMBNAIL = {
            "class": "thumbnail inline", "format": "jpg", "crop": "fill", "height": 150, "width": 150,
        },

        FRAME = {
            "class": "thumbnail inline", "format": "jpg", "crop": "fill", "height": 720, "width": 540,
        },

        EFFECTS = dict(
          format = "png",
          transformation = [
              dict(height=130, width=130, crop="thumb", radius=10,),
          ]
        ),
        MINIFRAME = {
            "class": "thumbnail inline", "format": "jpg", "crop": "fill", "height": 130, "width": 130,
        },

        SMALL_SERPIA = dict(
          format = "png",
          transformation = [
              dict(height=130, width=130, crop="thumb", radius=10, effect = "sepia"),
          ]
        ),

        BIG_SERPIA = dict(
          format = "png",
          transformation = [
              dict(crop="thumb",effect = "sepia"),
          ]
        ),

        default=dict(
          format='png',
          ),

        NORMAL=dict(
          format = "png",
          transformation = [
              dict(height=130, width=130, radius=10,),
          ]
          ),

    )



