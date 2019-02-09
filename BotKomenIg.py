<?php
 
/*
********************************************************
****|         SIMPLE BOT KOMEN INSTAGRAM           |****
              Author: Seputar-Informasi23
              Website: Seputar-Informasi23.blogspot.com
********************************************************
*/
 
$toket  = "token elo lah bro...";
$komeng = "hayyy @" . $nami . ", like back eaa kaka :D";
 
function curl($url, $post = null) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    if ($post != null) {
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
    }
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    $exec = curl_exec($ch);
    curl_close($ch);
    return $exec;
}
 
$curl   = curl("https://api.instagram.com/v1/users/self/feed?access_token=" . $toket);
$ngirim = json_decode($curl);
foreach ($ngirim->data as $data) {
    $nami = $data->username;
    $menta  = curl("https://api.instagram.com/v1/media/" . $data->id . "/comments", array(
        "access_token" => $token,
        "text" => urlencode($komeng)
    ));
    $ngirim = json_decode($menta);
    if ($ngirim->meta->code == "200")
        echo "Berhasil cooyy!!\n";
    else
        echo "Gagal komeng :((\n";
    sleep(2);
    }
?>
