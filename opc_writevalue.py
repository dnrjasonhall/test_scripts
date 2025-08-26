# Test reading one OPC value directly
opc_server = "ACM"

# Define app/array/register statically
app      = 11
array    = 3
register = 19

# Build the OPC item string
# Example: "3000303400.11:13:19"
opc_item = "3003034100.{0}:{1}:{2}".format(app, array, register)
#opc_item = "3000303400.{0}:{1}:{2}".format(app, array, register)
#opc_item = "HB.1103"

# Declare the system function parameters
oldQualifiedValue = system.opc.readValue(opc_server, opc_item)
print(oldQualifiedValue.getValue())
newValue = oldQualifiedValue.getValue() - 0.1
print("new value %s"%newValue)

# Call the system function and print out results
writeval = newValue
#writeval = 24.5
#writeval = True
returnQuality = system.opc.writeValue(opc_server, opc_item, writeval)

if returnQuality.isGood():
    print "Write was successful"
else:
   print "Write failed", writeval
