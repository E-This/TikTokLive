# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tiktok_schema.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13tiktok_schema.proto\x12\x06TikTok\"C\n\x17WebcastWebsocketMessage\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0c\n\x04type\x18\x07 \x01(\t\x12\x0e\n\x06\x62inary\x18\x08 \x01(\x0c\"/\n\x13WebcastWebsocketAck\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0c\n\x04type\x18\x07 \x01(\t\"\xf8\x02\n\x0fWebcastResponse\x12\x31\n\x08messages\x18\x01 \x03(\x0b\x32\x1f.TikTok.WebcastResponse.Message\x12\x0e\n\x06\x63ursor\x18\x02 \x01(\t\x12\x15\n\rfetchInterval\x18\x03 \x01(\x05\x12\x17\n\x0fserverTimestamp\x18\x04 \x01(\x03\x12\x13\n\x0binternalExt\x18\x05 \x01(\t\x12\x11\n\tfetchType\x18\x06 \x01(\x05\x12\x37\n\x07wsParam\x18\x07 \x01(\x0b\x32&.TikTok.WebcastResponse.WebsocketParam\x12\x19\n\x11heartbeatDuration\x18\x08 \x01(\x05\x12\x0f\n\x07needAck\x18\t \x01(\x08\x12\r\n\x05wsUrl\x18\n \x01(\t\x1a\'\n\x07Message\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06\x62inary\x18\x02 \x01(\x0c\x1a-\n\x0eWebsocketParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\"\n\x0bRoomMessage\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\'\n\x15WebcastControlMessage\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\x05\"\xbf\x01\n\x19WebcastRoomUserSeqMessage\x12@\n\x0btop_viewers\x18\x02 \x03(\x0b\x32+.TikTok.WebcastRoomUserSeqMessage.TopViewer\x12\x14\n\x0cviewer_count\x18\x03 \x01(\x05\x1aJ\n\tTopViewer\x12\x13\n\x0b\x63oins_given\x18\x01 \x01(\r\x12\x1a\n\x04user\x18\x02 \x01(\x0b\x32\x0c.TikTok.User\x12\x0c\n\x04rank\x18\x03 \x01(\r\"\xc3\x02\n\x12WebcastChatMessage\x12\x1a\n\x04user\x18\x02 \x01(\x0b\x32\x0c.TikTok.User\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x12\x1e\n\x08mentions\x18\x0c \x03(\x0b\x32\x0c.TikTok.User\x12\x34\n\x06images\x18\r \x03(\x0b\x32$.TikTok.WebcastChatMessage.ChatImage\x12\x10\n\x08language\x18\x0e \x01(\t\x1a\x97\x01\n\tChatImage\x12\x10\n\x08position\x18\x01 \x01(\x05\x12\x42\n\x05image\x18\x02 \x01(\x0b\x32\x33.TikTok.WebcastChatMessage.ChatImage.ChatImageImage\x1a\x34\n\x0e\x43hatImageImage\x12\"\n\x05image\x18\x02 \x01(\x0b\x32\x13.TikTok.TikTokImage\"\x82\x01\n\x14WebcastMemberMessage\x12*\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1b.TikTok.WebcastMessageEvent\x12\x1a\n\x04user\x18\x02 \x01(\x0b\x32\x0c.TikTok.User\x12\x0f\n\x07viewers\x18\x03 \x01(\x05\x12\x11\n\taction_id\x18\n \x01(\x05\"\xd2\x03\n\x12WebcastGiftMessage\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x13\n\x0brepeatCount\x18\x05 \x01(\x05\x12\x1a\n\x04user\x18\x07 \x01(\x0b\x32\x0c.TikTok.User\x12\x11\n\trepeatEnd\x18\t \x01(\x05\x12\x45\n\x04info\x18\x0f \x01(\x0b\x32\x37.TikTok.WebcastGiftMessage.WebcastGiftMessageGiftDetail\x12I\n\trecipient\x18\x17 \x01(\x0b\x32\x36.TikTok.WebcastGiftMessage.WebcastGiftMessageRecipient\x1a\x41\n\x1bWebcastGiftMessageRecipient\x12\x11\n\ttimestamp\x18\x06 \x01(\x04\x12\x0f\n\x07user_id\x18\x08 \x01(\x04\x1a\x96\x01\n\x1cWebcastGiftMessageGiftDetail\x12\"\n\x05image\x18\x01 \x01(\x0b\x32\x13.TikTok.TikTokImage\x12\x0c\n\x04name\x18\x10 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\x05\x12\x0c\n\x04type\x18\x0b \x01(\x05\x12\x15\n\rdiamond_count\x18\x0c \x01(\x05\"\xd6\x03\n\x14WebcastLinkMicBattle\x12K\n\x0b\x62\x61ttleUsers\x18\n \x03(\x0b\x32\x36.TikTok.WebcastLinkMicBattle.WebcastLinkMicBattleItems\x1a\xf0\x02\n\x19WebcastLinkMicBattleItems\x12\x65\n\x0b\x62\x61ttleGroup\x18\x02 \x01(\x0b\x32P.TikTok.WebcastLinkMicBattle.WebcastLinkMicBattleItems.WebcastLinkMicBattleGroup\x1a\xeb\x01\n\x19WebcastLinkMicBattleGroup\x12g\n\x04user\x18\x01 \x01(\x0b\x32Y.TikTok.WebcastLinkMicBattle.WebcastLinkMicBattleItems.WebcastLinkMicBattleGroup.LinkUser\x1a\x65\n\x08LinkUser\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12#\n\x06\x61vatar\x18\x03 \x01(\x0b\x32\x13.TikTok.TikTokImage\x12\x11\n\tunique_id\x18\x04 \x01(\t\"\xdd\x02\n\x14WebcastLinkMicArmies\x12K\n\x0b\x62\x61ttleItems\x18\x03 \x03(\x0b\x32\x36.TikTok.WebcastLinkMicArmies.WebcastLinkMicArmiesItems\x12\x14\n\x0c\x62\x61ttleStatus\x18\x07 \x01(\x05\x1a\xe1\x01\n\x19WebcastLinkMicArmiesItems\x12\x12\n\nhostUserId\x18\x01 \x01(\x04\x12\x66\n\x0c\x62\x61ttleGroups\x18\x02 \x03(\x0b\x32P.TikTok.WebcastLinkMicArmies.WebcastLinkMicArmiesItems.WebcastLinkMicArmiesGroup\x1aH\n\x19WebcastLinkMicArmiesGroup\x12\x1b\n\x05users\x18\x01 \x03(\x0b\x32\x0c.TikTok.User\x12\x0e\n\x06points\x18\x02 \x01(\x05\"w\n\x14WebcastSocialMessage\x12\x1a\n\x04user\x18\x02 \x01(\x0b\x32\x0c.TikTok.User\x12\x17\n\x0ftotal_followers\x18\x06 \x01(\r\x12*\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1b.TikTok.WebcastMessageEvent\"\x80\x01\n\x12WebcastLikeMessage\x12\x1a\n\x04user\x18\x05 \x01(\x0b\x32\x0c.TikTok.User\x12*\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1b.TikTok.WebcastMessageEvent\x12\r\n\x05likes\x18\x02 \x01(\x05\x12\x13\n\x0btotal_likes\x18\x03 \x01(\x05\"\xa8\x01\n\x19WebcastQuestionNewMessage\x12J\n\x0fquestionDetails\x18\x02 \x01(\x0b\x32\x31.TikTok.WebcastQuestionNewMessage.QuestionDetails\x1a?\n\x0fQuestionDetails\x12\x10\n\x08question\x18\x02 \x01(\t\x12\x1a\n\x04user\x18\x05 \x01(\x0b\x32\x0c.TikTok.User\"\xde\x01\n\x17WebcastLiveIntroMessage\x12\x0f\n\x07room_id\x18\x02 \x01(\x04\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x1e\n\x08streamer\x18\x05 \x01(\x0b\x32\x0c.TikTok.User\x12\x10\n\x08language\x18\x08 \x01(\t\x12=\n\nextra_info\x18\x07 \x01(\x0b\x32).TikTok.WebcastLiveIntroMessage.IntroData\x1a\x30\n\tIntroData\x12#\n\x07\x64\x65tails\x18\x15 \x01(\x0b\x32\x12.TikTok.ValueLabel\"$\n\rSystemMessage\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"*\n\x1aWebcastInRoomBannerMessage\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"\xdb\x04\n\x16WebcastRankTextMessage\x12K\n\x0c\x64\x65tailsSmall\x18\x05 \x01(\x0b\x32\x35.TikTok.WebcastRankTextMessage.RankTextMessageSummary\x12?\n\x07\x64\x65tails\x18\x06 \x01(\x0b\x32..TikTok.WebcastRankTextMessage.RankTextMessage\x12\x0b\n\x03id1\x18\x07 \x01(\x04\x1aZ\n\x16RankTextMessageSummary\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12#\n\x07\x64\x65tails\x18\x04 \x01(\x0b\x32\x12.TikTok.ValueLabel\x1a\xc9\x02\n\x0fRankTextMessage\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12N\n\x07\x64\x65tails\x18\x04 \x03(\x0b\x32=.TikTok.WebcastRankTextMessage.RankTextMessage.MessageDetails\x1a\xc8\x01\n\x0eMessageDetails\x12\r\n\x05\x64\x61ta1\x18\x01 \x01(\r\x12\x10\n\x08\x63\x61tegory\x18\x0b \x01(\t\x12Y\n\x04user\x18\x15 \x01(\x0b\x32K.TikTok.WebcastRankTextMessage.RankTextMessage.MessageDetails.UserContainer\x1a:\n\rUserContainer\x12\x1a\n\x04user\x18\x01 \x01(\x0b\x32\x0c.TikTok.User\x12\r\n\x05\x64\x61ta1\x18\x02 \x01(\r\"\x8a\x01\n\x18WebcastRankUpdateMessage\x12=\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32/.TikTok.WebcastRankUpdateMessage.RankUpdateData\x1a/\n\x0eRankUpdateData\x12\x1d\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x0f.TikTok.Ranking\"\x88\x01\n\x18WebcastHourlyRankMessage\x12<\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32..TikTok.WebcastHourlyRankMessage.RankContainer\x1a.\n\rRankContainer\x12\x1d\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x0f.TikTok.Ranking\"\xf8\x01\n\x17WebcastEmoteChatMessage\x12\x1a\n\x04user\x18\x02 \x01(\x0b\x32\x0c.TikTok.User\x12;\n\x05\x65mote\x18\x03 \x01(\x0b\x32,.TikTok.WebcastEmoteChatMessage.EmoteDetails\x1a\x83\x01\n\x0c\x45moteDetails\x12\x10\n\x08\x65mote_id\x18\x01 \x01(\t\x12\x46\n\x05image\x18\x02 \x01(\x0b\x32\x37.TikTok.WebcastEmoteChatMessage.EmoteDetails.EmoteImage\x1a\x19\n\nEmoteImage\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x82\x05\n\x16WebcastEnvelopeMessage\x12G\n\x0ftreasureBoxData\x18\x02 \x01(\x0b\x32..TikTok.WebcastEnvelopeMessage.TreasureBoxData\x12G\n\x0ftreasureBoxUser\x18\x01 \x01(\x0b\x32..TikTok.WebcastEnvelopeMessage.TreasureBoxUser\x1a\x8e\x03\n\x0fTreasureBoxUser\x12N\n\x05user2\x18\x08 \x01(\x0b\x32?.TikTok.WebcastEnvelopeMessage.TreasureBoxUser.TreasureBoxUser2\x1a\xaa\x02\n\x10TreasureBoxUser2\x12_\n\x05user3\x18\x04 \x03(\x0b\x32P.TikTok.WebcastEnvelopeMessage.TreasureBoxUser.TreasureBoxUser2.TreasureBoxUser3\x1a\xb4\x01\n\x10TreasureBoxUser3\x12p\n\x05user4\x18\x15 \x01(\x0b\x32\x61.TikTok.WebcastEnvelopeMessage.TreasureBoxUser.TreasureBoxUser2.TreasureBoxUser3.TreasureBoxUser4\x1a.\n\x10TreasureBoxUser4\x12\x1a\n\x04user\x18\x01 \x01(\x0b\x32\x0c.TikTok.User\x1a\x45\n\x0fTreasureBoxData\x12\r\n\x05\x63oins\x18\x05 \x01(\r\x12\x10\n\x08openable\x18\x06 \x01(\r\x12\x11\n\ttimestamp\x18\x07 \x01(\x04\"(\n\x0bTikTokImage\x12\x0c\n\x04urls\x18\x01 \x03(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\"\xa1\x01\n\x13WebcastMessageEvent\x12G\n\x07\x64\x65tails\x18\x08 \x01(\x0b\x32\x36.TikTok.WebcastMessageEvent.WebcastMessageEventDetails\x1a\x41\n\x1aWebcastMessageEventDetails\x12\x14\n\x0c\x64isplay_type\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\"\xcf\x05\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12#\n\x06\x61vatar\x18\t \x01(\x0b\x32\x13.TikTok.TikTokImage\x12#\n\x04info\x18\x16 \x01(\x0b\x32\x15.TikTok.User.UserInfo\x12\x11\n\tunique_id\x18& \x01(\t\x12\x0f\n\x07sec_uid\x18. \x01(\t\x12&\n\x06\x62\x61\x64ges\x18@ \x03(\x0b\x32\x16.TikTok.User.UserBadge\x1a\x45\n\x08UserInfo\x12\x11\n\tfollowing\x18\x01 \x01(\x05\x12\x11\n\tfollowers\x18\x02 \x01(\x05\x12\x13\n\x0b\x66ollow_role\x18\x03 \x01(\x05\x1a\xc6\x03\n\tUserBadge\x12\x18\n\x10\x62\x61\x64ge_scene_type\x18\x03 \x01(\x05\x12.\n\x04text\x18\x15 \x01(\x0b\x32 .TikTok.User.UserBadge.BadgeText\x12\x30\n\x05image\x18\x14 \x01(\x0b\x32!.TikTok.User.UserBadge.BadgeImage\x12\x34\n\x07\x63omplex\x18\x17 \x01(\x0b\x32#.TikTok.User.UserBadge.BadgeComplex\x1a(\n\tBadgeText\x12\r\n\x05label\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x1a\x30\n\nBadgeImage\x12\"\n\x05image\x18\x02 \x01(\x0b\x32\x13.TikTok.TikTokImage\x1a\xaa\x01\n\x0c\x42\x61\x64geComplex\x12\"\n\x05image\x18\x02 \x01(\x0b\x32\x13.TikTok.TikTokImage\x12=\n\x05label\x18\x03 \x01(\x0b\x32..TikTok.User.UserBadge.BadgeComplex.BadgeLabel\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\x1a)\n\nBadgeLabel\x12\r\n\x05label\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xa4\x01\n\x07Ranking\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12+\n\x05\x65xtra\x18\x03 \x01(\x0b\x32\x1c.TikTok.Ranking.TikTokColour\x12#\n\x07\x64\x65tails\x18\x04 \x03(\x0b\x32\x12.TikTok.ValueLabel\x1a*\n\x0cTikTokColour\x12\x0e\n\x06\x63olour\x18\x01 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\x04\"I\n\nValueLabel\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\r\x12\r\n\x05label\x18\x02 \x01(\t\x12\x0e\n\x06label2\x18\x03 \x01(\t\x12\x0e\n\x06label3\x18\x0b \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tiktok_schema_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_WEBCASTWEBSOCKETMESSAGE']._serialized_start=31
  _globals['_WEBCASTWEBSOCKETMESSAGE']._serialized_end=98
  _globals['_WEBCASTWEBSOCKETACK']._serialized_start=100
  _globals['_WEBCASTWEBSOCKETACK']._serialized_end=147
  _globals['_WEBCASTRESPONSE']._serialized_start=150
  _globals['_WEBCASTRESPONSE']._serialized_end=526
  _globals['_WEBCASTRESPONSE_MESSAGE']._serialized_start=440
  _globals['_WEBCASTRESPONSE_MESSAGE']._serialized_end=479
  _globals['_WEBCASTRESPONSE_WEBSOCKETPARAM']._serialized_start=481
  _globals['_WEBCASTRESPONSE_WEBSOCKETPARAM']._serialized_end=526
  _globals['_ROOMMESSAGE']._serialized_start=528
  _globals['_ROOMMESSAGE']._serialized_end=562
  _globals['_WEBCASTCONTROLMESSAGE']._serialized_start=564
  _globals['_WEBCASTCONTROLMESSAGE']._serialized_end=603
  _globals['_WEBCASTROOMUSERSEQMESSAGE']._serialized_start=606
  _globals['_WEBCASTROOMUSERSEQMESSAGE']._serialized_end=797
  _globals['_WEBCASTROOMUSERSEQMESSAGE_TOPVIEWER']._serialized_start=723
  _globals['_WEBCASTROOMUSERSEQMESSAGE_TOPVIEWER']._serialized_end=797
  _globals['_WEBCASTCHATMESSAGE']._serialized_start=800
  _globals['_WEBCASTCHATMESSAGE']._serialized_end=1123
  _globals['_WEBCASTCHATMESSAGE_CHATIMAGE']._serialized_start=972
  _globals['_WEBCASTCHATMESSAGE_CHATIMAGE']._serialized_end=1123
  _globals['_WEBCASTCHATMESSAGE_CHATIMAGE_CHATIMAGEIMAGE']._serialized_start=1071
  _globals['_WEBCASTCHATMESSAGE_CHATIMAGE_CHATIMAGEIMAGE']._serialized_end=1123
  _globals['_WEBCASTMEMBERMESSAGE']._serialized_start=1126
  _globals['_WEBCASTMEMBERMESSAGE']._serialized_end=1256
  _globals['_WEBCASTGIFTMESSAGE']._serialized_start=1259
  _globals['_WEBCASTGIFTMESSAGE']._serialized_end=1725
  _globals['_WEBCASTGIFTMESSAGE_WEBCASTGIFTMESSAGERECIPIENT']._serialized_start=1507
  _globals['_WEBCASTGIFTMESSAGE_WEBCASTGIFTMESSAGERECIPIENT']._serialized_end=1572
  _globals['_WEBCASTGIFTMESSAGE_WEBCASTGIFTMESSAGEGIFTDETAIL']._serialized_start=1575
  _globals['_WEBCASTGIFTMESSAGE_WEBCASTGIFTMESSAGEGIFTDETAIL']._serialized_end=1725
  _globals['_WEBCASTLINKMICBATTLE']._serialized_start=1728
  _globals['_WEBCASTLINKMICBATTLE']._serialized_end=2198
  _globals['_WEBCASTLINKMICBATTLE_WEBCASTLINKMICBATTLEITEMS']._serialized_start=1830
  _globals['_WEBCASTLINKMICBATTLE_WEBCASTLINKMICBATTLEITEMS']._serialized_end=2198
  _globals['_WEBCASTLINKMICBATTLE_WEBCASTLINKMICBATTLEITEMS_WEBCASTLINKMICBATTLEGROUP']._serialized_start=1963
  _globals['_WEBCASTLINKMICBATTLE_WEBCASTLINKMICBATTLEITEMS_WEBCASTLINKMICBATTLEGROUP']._serialized_end=2198
  _globals['_WEBCASTLINKMICBATTLE_WEBCASTLINKMICBATTLEITEMS_WEBCASTLINKMICBATTLEGROUP_LINKUSER']._serialized_start=2097
  _globals['_WEBCASTLINKMICBATTLE_WEBCASTLINKMICBATTLEITEMS_WEBCASTLINKMICBATTLEGROUP_LINKUSER']._serialized_end=2198
  _globals['_WEBCASTLINKMICARMIES']._serialized_start=2201
  _globals['_WEBCASTLINKMICARMIES']._serialized_end=2550
  _globals['_WEBCASTLINKMICARMIES_WEBCASTLINKMICARMIESITEMS']._serialized_start=2325
  _globals['_WEBCASTLINKMICARMIES_WEBCASTLINKMICARMIESITEMS']._serialized_end=2550
  _globals['_WEBCASTLINKMICARMIES_WEBCASTLINKMICARMIESITEMS_WEBCASTLINKMICARMIESGROUP']._serialized_start=2478
  _globals['_WEBCASTLINKMICARMIES_WEBCASTLINKMICARMIESITEMS_WEBCASTLINKMICARMIESGROUP']._serialized_end=2550
  _globals['_WEBCASTSOCIALMESSAGE']._serialized_start=2552
  _globals['_WEBCASTSOCIALMESSAGE']._serialized_end=2671
  _globals['_WEBCASTLIKEMESSAGE']._serialized_start=2674
  _globals['_WEBCASTLIKEMESSAGE']._serialized_end=2802
  _globals['_WEBCASTQUESTIONNEWMESSAGE']._serialized_start=2805
  _globals['_WEBCASTQUESTIONNEWMESSAGE']._serialized_end=2973
  _globals['_WEBCASTQUESTIONNEWMESSAGE_QUESTIONDETAILS']._serialized_start=2910
  _globals['_WEBCASTQUESTIONNEWMESSAGE_QUESTIONDETAILS']._serialized_end=2973
  _globals['_WEBCASTLIVEINTROMESSAGE']._serialized_start=2976
  _globals['_WEBCASTLIVEINTROMESSAGE']._serialized_end=3198
  _globals['_WEBCASTLIVEINTROMESSAGE_INTRODATA']._serialized_start=3150
  _globals['_WEBCASTLIVEINTROMESSAGE_INTRODATA']._serialized_end=3198
  _globals['_SYSTEMMESSAGE']._serialized_start=3200
  _globals['_SYSTEMMESSAGE']._serialized_end=3236
  _globals['_WEBCASTINROOMBANNERMESSAGE']._serialized_start=3238
  _globals['_WEBCASTINROOMBANNERMESSAGE']._serialized_end=3280
  _globals['_WEBCASTRANKTEXTMESSAGE']._serialized_start=3283
  _globals['_WEBCASTRANKTEXTMESSAGE']._serialized_end=3886
  _globals['_WEBCASTRANKTEXTMESSAGE_RANKTEXTMESSAGESUMMARY']._serialized_start=3464
  _globals['_WEBCASTRANKTEXTMESSAGE_RANKTEXTMESSAGESUMMARY']._serialized_end=3554
  _globals['_WEBCASTRANKTEXTMESSAGE_RANKTEXTMESSAGE']._serialized_start=3557
  _globals['_WEBCASTRANKTEXTMESSAGE_RANKTEXTMESSAGE']._serialized_end=3886
  _globals['_WEBCASTRANKTEXTMESSAGE_RANKTEXTMESSAGE_MESSAGEDETAILS']._serialized_start=3686
  _globals['_WEBCASTRANKTEXTMESSAGE_RANKTEXTMESSAGE_MESSAGEDETAILS']._serialized_end=3886
  _globals['_WEBCASTRANKTEXTMESSAGE_RANKTEXTMESSAGE_MESSAGEDETAILS_USERCONTAINER']._serialized_start=3828
  _globals['_WEBCASTRANKTEXTMESSAGE_RANKTEXTMESSAGE_MESSAGEDETAILS_USERCONTAINER']._serialized_end=3886
  _globals['_WEBCASTRANKUPDATEMESSAGE']._serialized_start=3889
  _globals['_WEBCASTRANKUPDATEMESSAGE']._serialized_end=4027
  _globals['_WEBCASTRANKUPDATEMESSAGE_RANKUPDATEDATA']._serialized_start=3980
  _globals['_WEBCASTRANKUPDATEMESSAGE_RANKUPDATEDATA']._serialized_end=4027
  _globals['_WEBCASTHOURLYRANKMESSAGE']._serialized_start=4030
  _globals['_WEBCASTHOURLYRANKMESSAGE']._serialized_end=4166
  _globals['_WEBCASTHOURLYRANKMESSAGE_RANKCONTAINER']._serialized_start=4120
  _globals['_WEBCASTHOURLYRANKMESSAGE_RANKCONTAINER']._serialized_end=4166
  _globals['_WEBCASTEMOTECHATMESSAGE']._serialized_start=4169
  _globals['_WEBCASTEMOTECHATMESSAGE']._serialized_end=4417
  _globals['_WEBCASTEMOTECHATMESSAGE_EMOTEDETAILS']._serialized_start=4286
  _globals['_WEBCASTEMOTECHATMESSAGE_EMOTEDETAILS']._serialized_end=4417
  _globals['_WEBCASTEMOTECHATMESSAGE_EMOTEDETAILS_EMOTEIMAGE']._serialized_start=4392
  _globals['_WEBCASTEMOTECHATMESSAGE_EMOTEDETAILS_EMOTEIMAGE']._serialized_end=4417
  _globals['_WEBCASTENVELOPEMESSAGE']._serialized_start=4420
  _globals['_WEBCASTENVELOPEMESSAGE']._serialized_end=5062
  _globals['_WEBCASTENVELOPEMESSAGE_TREASUREBOXUSER']._serialized_start=4593
  _globals['_WEBCASTENVELOPEMESSAGE_TREASUREBOXUSER']._serialized_end=4991
  _globals['_WEBCASTENVELOPEMESSAGE_TREASUREBOXUSER_TREASUREBOXUSER2']._serialized_start=4693
  _globals['_WEBCASTENVELOPEMESSAGE_TREASUREBOXUSER_TREASUREBOXUSER2']._serialized_end=4991
  _globals['_WEBCASTENVELOPEMESSAGE_TREASUREBOXUSER_TREASUREBOXUSER2_TREASUREBOXUSER3']._serialized_start=4811
  _globals['_WEBCASTENVELOPEMESSAGE_TREASUREBOXUSER_TREASUREBOXUSER2_TREASUREBOXUSER3']._serialized_end=4991
  _globals['_WEBCASTENVELOPEMESSAGE_TREASUREBOXUSER_TREASUREBOXUSER2_TREASUREBOXUSER3_TREASUREBOXUSER4']._serialized_start=4945
  _globals['_WEBCASTENVELOPEMESSAGE_TREASUREBOXUSER_TREASUREBOXUSER2_TREASUREBOXUSER3_TREASUREBOXUSER4']._serialized_end=4991
  _globals['_WEBCASTENVELOPEMESSAGE_TREASUREBOXDATA']._serialized_start=4993
  _globals['_WEBCASTENVELOPEMESSAGE_TREASUREBOXDATA']._serialized_end=5062
  _globals['_TIKTOKIMAGE']._serialized_start=5064
  _globals['_TIKTOKIMAGE']._serialized_end=5104
  _globals['_WEBCASTMESSAGEEVENT']._serialized_start=5107
  _globals['_WEBCASTMESSAGEEVENT']._serialized_end=5268
  _globals['_WEBCASTMESSAGEEVENT_WEBCASTMESSAGEEVENTDETAILS']._serialized_start=5203
  _globals['_WEBCASTMESSAGEEVENT_WEBCASTMESSAGEEVENTDETAILS']._serialized_end=5268
  _globals['_USER']._serialized_start=5271
  _globals['_USER']._serialized_end=5990
  _globals['_USER_USERINFO']._serialized_start=5464
  _globals['_USER_USERINFO']._serialized_end=5533
  _globals['_USER_USERBADGE']._serialized_start=5536
  _globals['_USER_USERBADGE']._serialized_end=5990
  _globals['_USER_USERBADGE_BADGETEXT']._serialized_start=5727
  _globals['_USER_USERBADGE_BADGETEXT']._serialized_end=5767
  _globals['_USER_USERBADGE_BADGEIMAGE']._serialized_start=5769
  _globals['_USER_USERBADGE_BADGEIMAGE']._serialized_end=5817
  _globals['_USER_USERBADGE_BADGECOMPLEX']._serialized_start=5820
  _globals['_USER_USERBADGE_BADGECOMPLEX']._serialized_end=5990
  _globals['_USER_USERBADGE_BADGECOMPLEX_BADGELABEL']._serialized_start=5949
  _globals['_USER_USERBADGE_BADGECOMPLEX_BADGELABEL']._serialized_end=5990
  _globals['_RANKING']._serialized_start=5993
  _globals['_RANKING']._serialized_end=6157
  _globals['_RANKING_TIKTOKCOLOUR']._serialized_start=6115
  _globals['_RANKING_TIKTOKCOLOUR']._serialized_end=6157
  _globals['_VALUELABEL']._serialized_start=6159
  _globals['_VALUELABEL']._serialized_end=6232
# @@protoc_insertion_point(module_scope)
