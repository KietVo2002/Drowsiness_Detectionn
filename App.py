import cv2

# Địa chỉ IP của camera
camera_ip = 'your_camera_ip_address'

# Khởi tạo kết nối đến camera
cap = cv2.VideoCapture(f'rtsp://{camera_ip}/live')

while True:
    # Đọc frame từ camera
    ret, frame = cap.read()
    
    # Hiển thị frame
    cv2.imshow('Camera', frame)
    
    # Thoát khỏi vòng lặp khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng camera và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()
