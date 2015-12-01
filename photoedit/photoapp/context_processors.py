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


        default=dict(
          format='png',
          ),

        NORMAL=dict(
          format = "png",
          transformation = [
              dict(height=130, width=130, radius=10,),
          ]
          ),
        #EFFECTS, EFFECT1
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
        #EFFECT2
        S_GRAYSCALE = dict(
          format = "png",
          transformation = [
              dict(height=130, width=130, crop="thumb", radius=10, effect = "grayscale"),
          ]
        ),

        B_GRAYSCALE = dict(
          format = "png",
          transformation = [
              dict(crop="thumb",effect = "grayscale"),
          ]
        ),
      #EFFECT3
      S_VIGNETTE = dict(
          format = "png",
          transformation = [
              dict(height=130, width=130, crop="thumb", radius=10, effect = "vignette"),
          ]
        ),

        B_VIGNETTE = dict(
          format = "png",
          transformation = [
              dict(crop="thumb",effect = "vignette"),
          ]
        ),

      #EFFECT4
      S_GRADIENTFADE = dict(
          format = "png",
          transformation = [
              dict(height=130, width=130, crop="thumb", radius=10, effect = "gradient_fade"),
          ]
        ),

        B_GRADIENTFADE = dict(
          format = "png",
          transformation = [
              dict(crop="thumb",effect = "gradient_fade"),
          ]
        ),

      #EFFECT5
      S_CONTRAST_70 = dict(
          format = "png",
          transformation = [
              dict(height=130, width=130, crop="thumb", radius=10, effect = "contrast:-70"),
          ]
        ),

        B_CONTRAST_70 = dict(
          format = "png",
          transformation = [
              dict(crop="thumb",effect = "contrast:-70"),
          ]
        ),


        #FILTER1
        S_BRIGHTNESS60 = dict(
          format = "png",
          transformation = [
              dict(height=130, width=130, crop="thumb", radius=10, effect = "brightness:60"),
          ]
        ),

        B_BRIGHTNESS60 = dict(
          format = "png",
          transformation = [
              dict(crop="thumb",effect = "brightness:60"),
          ]
        ),
    
        #FILTER2
        S_BLUR = dict(
          format = "png",
          transformation = [
              dict(height=130, width=130, crop="thumb", radius=10, effect = "blur:200"),
          ]
        ),

        B_BLUR = dict(
          format = "png",
          transformation = [
              dict(crop="thumb",effect = "blur:200"),
          ]
        ),

        #FILTER3
        S_RED = dict(
          format = "png",
          transformation = [
              dict(height=130, width=130, crop="thumb", radius=10, effect = "red:50"),
          ]
        ),

        B_RED = dict(
          format = "png",
          transformation = [
              dict(crop="thumb",effect = "red:50"),
          ]
        ),

        #FILTER4
        S_GREEN = dict(
          format = "png",
          transformation = [
              dict(height=130, width=130, crop="thumb", radius=10, effect = "green:50"),
          ]
        ),

        B_GREEN = dict(
          format = "png",
          transformation = [
              dict(crop="thumb",effect = "green:90"),
          ]
        ),

        #FILTER5
        S_BLUE = dict(
          format = "png",
          transformation = [
              dict(height=130, width=130, crop="thumb", radius=10, effect = "blue:90"),
          ]
        ),

        B_BLUE = dict(
          format = "png",
          transformation = [
              dict(crop="thumb",effect = "blue:90"),
          ]
        ),

)

