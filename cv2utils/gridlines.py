import cv2

def showimage(imgarr, title="Example"):
    cv2.imshow(title, imgarr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def overlay_gridlines(image_path, grid_size=13, lineThickness=1, color=(0, 255, 0), alpha=0.4):
    # Draws gridlines onto image as if image were split uniformly into a NxN grid, where N=grid_size.
    image = cv2.imread(image_path)
    overlay = image.copy()

    # optional params
    gs = grid_size
    lineThickness = lineThickness
    color = color
    alpha = alpha

    w, h, numchannels = image.shape
    gw = w // gs
    gh = h // gs
    # vertical lines
    for i in range(1, gs):
        overlay = cv2.line(overlay, (i * gw, 0), (i * gw, h), color, lineThickness)

    # horizontal lines:
    for i in range(1, gs):
        overlay = cv2.line(overlay, (0, i * gh), (w, i * gh), color, lineThickness)

    # overlay
    image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

    return image_new


if __name__ == '__main__':
    # sample function call
    new1 = overlay_gridlines("../sample_416.png", color=(255, 0, 0), alpha=0.2)
    # save
    cv2.imwrite(f'../gridlines.png', new1)
