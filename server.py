import asyncio
import websockets

# قائمة لحفظ الاتصالات النشطة (الموبايل واللابتوب)
connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # إعادة إرسال أي رسالة أو أمر لكل الأجهزة المتصلة (مثل نقل الأوامر بين الموبايل واللابتوب)
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

async def main():
    # تشغيل السيرفر على البورت الافتراضي للمنصة
    async with websockets.serve(handler, "0.0.0.0", 10000):
        await asyncio.Future()  # تشغيل دائم

if __name__ == "__main__":
    asyncio.run(main())