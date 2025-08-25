# Test reading one OPC value directly
opc_server = "ACM"

# Define app/array/register statically
app      = 9
array    = 0
register = 9

# Build the OPC item string
# Example: "3000303400.11:13:19"
opc_item = "3000303400.{0}:{1}:{2}".format(app, array, register)

# Fix formatting in case there are $ characters
opc_item = opc_item.replace("$", ".$")

# Read the value
qv = system.opc.readValues(opc_server, [opc_item])[0]

# Print out the details
print "Item:      ", opc_item
print "Value:     ", qv.value
print "Type:      ", type(qv.value)
print "Quality:   ", qv.quality
print "Timestamp: ", qv.timestamp
