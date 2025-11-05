#!/bin/bash

# Directory containing individual service files
SERVICE_DIR="services"
mkdir $SERVICE_DIR/lists

# Directory to output combined category files
OUTPUT_DIR="services/categories"
mkdir $OUTPUT_DIR


# Define categories and associated service filenames
declare -A categories
categories["social_media"]="facebook.txt instagram.txt twitter.txt tiktok.txt snapchat.txt mastodon.txt linkedin.txt vk.txt weibo.txt qq.txt clubhouse.txt kook.txt line.txt kik.txt kakaotalk.txt viber.txt wizz.txt xiaohongshu.txt tumblr.txt"
categories["ai"]="chatgpt.txt claude.txt deepseek.txt"
categories["streaming_video"]="youtube.txt netflix.txt hulu.txt disneyplus.txt disney_streaming.txt amazon_streaming.txt apple_streaming.txt hbomax.txt discoveryplus.txt canais_globo.txt globoplay.txt crunchyroll.txt dailymotion.txt lionsgateplus.txt looke.txt nebula.txt paramountplus.txt peacock_tv.txt plex.txt pluto_tv.txt samsung_tv_plus.txt rakuten_viki.txt spotify_video.txt"
categories["messaging"]="discord.txt slack.txt wechat.txt signal.txt telegram.txt whatsapp.txt skype.txt" 
categories["gaming"]="origin.txt activision_blizzard.txt blizzard_entertainment.txt battle_net.txt epic_games.txt electronic_arts.txt fifa.txt leagueoflegends.txt riot_games.txt roblox.txt rockstar_games.txt steam.txt playstation.txt xboxlive.txt nintendo.txt minecraft.txt nvidia.txt ubisoft.txt valorant.txt wargaming.txt"

categories["shopping"]="amazon.txt aliexpress.txt shopee.txt lazada.txt shein.txt mercado_libre.txt temu.txt ebay.txt"

categories["cloud_storage"]="dropbox.txt box.txt playstore.txt icloud_private_relay.txt"

categories["adult_dating"]="onlyfans.txt plenty_of_fish.txt tinder.txt"

categories["music_audio"]="spotify.txt deezer.txt soundcloud.txt tidal.txt iheartradio.txt"

categories["news_sports"]="espn.txt zhihu.txt"

categories["misc"]="4chan.txt 9gag.txt amino.txt bigo_live.txt douban.txt imgur.txt coolapk.txt odysee.txt olvid.txt"

# Loop through categories
for category in "${!categories[@]}"; do
    echo "Building $category..."
    output_file="$OUTPUT_DIR/${category}.txt"
    : > "$output_file"  # safely truncate the output file

    # Loop over each service file in the category
    for service_file in ${categories[$category]}; do
        full_path="$SERVICE_DIR/$service_file"
        if [[ -f "$full_path" ]]; then
            # Append contents, omitting lines starting with # or |
            grep -Ev '^(#|\|)' "$full_path" >> "$output_file"
            
            # Move processed file into services/lists/
            mv "$full_path" "$SERVICE_DIR/lists/"
            echo "  Moved $service_file → services/lists/"
        else
            echo "  ⚠️  Missing file: $full_path"
        fi
    done

    echo "✅ $category built."
done

echo "All categories built successfully!"
