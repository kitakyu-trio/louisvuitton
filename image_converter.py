from PIL import Image, ImageChops

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def cropImage(image): #引数は画像の相対パス
    # 背景色画像を作成
    bg = Image.new("RGBA", image.size, image.getpixel((0, 0)))
    # bg.show()

    # 背景色画像と元画像の差分画像を作成
    diff = ImageChops.difference(image, bg)
    # diff.show()

    # 背景色との境界を求めて画像を切り抜く
    croprange = diff.convert("RGBA").getbbox()
    crop_image = image.crop(croprange)
    # crop_image.show()

    return crop_image

def LeadImage(num,brand,bot_name):
    path = '/Users/endoutakumi/Desktop/scraping/study/scrayping_file/scraping_result/item_image/' + bot_name + '/' + brand + '/image/' + str(num).zfill(5)

    img = Image.open(path + '/image000.png')
    frame = Image.open('/Users/endoutakumi/Desktop/scraping/study/scrayping_file/img_content/frame/simple_gold.png')
    logo = Image.open('/Users/endoutakumi/Desktop/scraping/study/scrayping_file/logo/' + brand + '.png')

    new_img = img.copy()
    new_img.thumbnail((600,1000))
    new_img = new_img.resize((430, 430))

    logo_image = logo.copy()
    logo_image = logo.resize((400,160))

    frame.paste(new_img,(160,250))
    frame.paste(logo_image,(175,70))
    frame.save(path + '/image.png')
    #frame.show()

    """
    new_img = img.copy()
    w1,h1 = 600,1000
    new_img.thumbnail((w1,h1))
    W_1 = w1
    new_img = crop_center(new_img,W_1,W_1)
    new_img.putalpha(alpha=255)


    crop_image = cropImage(new_img)
    #print(crop_image.size,crop_image.mode)

    logo_image = logo.copy()
    crop_logo = cropImage(logo_image)
    #print(crop_logo.width,crop_logo.mode)


    bg = Image.new("RGBA", (750,750), new_img.getpixel((0, 0)))
    center_W_1 = int((750-crop_image.width)/2)
    center_H_1 = int((750-crop_image.height)/2)
    bg.paste(crop_image,(center_W_1,center_H_1),crop_image)

    center_W_2 = int((750-crop_logo.width)/2)
    center_H_2 = int(200/2)
    bg.paste(crop_logo,(center_W_2,center_H_2),crop_logo)


    c = Image.new('RGBA', (750,750), (255, 255, 255,0))
    c.paste(frame, (0,0), frame)


    result = Image.alpha_composite(bg, c)
    result.save(path + '/image.png')
    #result.show()
    """