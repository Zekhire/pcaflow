import pcaflow.utils.flow_io as flow_io
import pcaflow.utils.viz_flow as viz_flow
import cv2



filename = "/home/zekhire/PycharmProjects/PWC-Net/Caffe/tmp/frame_0010_forward.flo"
u, v = flow_io.flow_read(filename)
optical_flow = viz_flow.viz_flow(u,v)


filename = "/home/zekhire/PycharmProjects/PWC-Net/Caffe/tmp/reference_frame_0010_forward.flo"
u, v = flow_io.flow_read(filename)
optical_flow_ref = viz_flow.viz_flow(u,v)

cv2.imshow("optical_flow", optical_flow)
cv2.imshow("optical_flow_ref", optical_flow_ref)
cv2.waitKey(0)