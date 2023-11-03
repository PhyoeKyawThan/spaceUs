import React from "react";
import { View, FlatList, StyleSheet, StatusBar, Text, Image } from "react-native";
import Post from "./src/Post";

const DATA = [
  {
    id: 0,
    username: "Dom AK",
    profile: "https://i.ibb.co/86SfTtx/wallpaperflare-com-wallpaper.jpg",
    content: {
      caption: "Hello World",
      image: "https://i.ibb.co/86SfTtx/wallpaperflare-com-wallpaper.jpg",
    },
    love: false,
    interested: false,
  },
  {
    id: 1,
    username: "Audrey",
    profile: "https://i.ibb.co/86SfTtx/wallpaperflare-com-wallpaper.jpg",
    content: {
      caption: "Nice Day",
      image: "https://i.ibb.co/86SfTtx/wallpaperflare-com-wallpaper.jpg",
    },
    love: false,
    interested: false,
  },
  // Add more post objects here
];


const App = () => {
  return (
    <View style={styles.container}>
      <FlatList data={DATA} renderItem={({ item }) => <Post data={item}/>} keyExtractor={(item)=> item.id.toString()}/>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginTop: StatusBar.currentHeight,
    flexDirection: "column",
    // alignItems: "center"
  },
});

export default App;
