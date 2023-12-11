cc_no = input("Enter the credit card number : ")
#out_1 = cc_no(0,3) + ' ' + cc_no(4,7) + ' ' + cc_no(8,11) +' ' + cc_no(12,15)
#out_1 = str(cc_no[0:4])
#print(out_1)
out = cc_no[0:4] + ' ' + cc_no[4:8] + ' ' + cc_no[8:12] +' ' + cc_no[12:16] 
req_out = str('.'*4) + ' ' + str('.'*4) + ' ' + str('.'*4) + ' ' + cc_no[12:16] 
print(out)
print(req_out)

