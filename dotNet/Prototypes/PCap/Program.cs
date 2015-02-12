using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using SharpPcap;

namespace PCap
{
    class Program
    {
        static void Main(string[] args)
        {
            var devices = CaptureDeviceList.Instance;

            foreach (ICaptureDevice dev in devices)
            {
                if (dev is SharpPcap.AirPcap.AirPcapDevice)
                {
                    Console.WriteLine("AIR - {0}", dev.Name);
                }
                else if (dev is SharpPcap.LibPcap.LibPcapLiveDevice)
                {
                    Console.WriteLine("LIB - {0}", dev.Name);
                }
                else if (dev is SharpPcap.WinPcap.WinPcapDevice)
                {
                    Console.WriteLine("WIN - {0}", dev.Name);
                }
            }

            var device = devices[1];

            device.OnPacketArrival += Program_OnPacketArrival;
            device.Open(DeviceMode.Promiscuous);

            device.StartCapture();

            Console.ReadKey();
            device.StopCapture();
        }

        static void Program_OnPacketArrival(object sender, CaptureEventArgs e)
        {
            Console.WriteLine("{0}", e.Packet.Timeval.ToString());
            //var packet = PacketDotNet.Packet.ParsePacket(PacketDotNet.LinkLayers.Ethernet, e.Packet.Data);
        }
    }
}
