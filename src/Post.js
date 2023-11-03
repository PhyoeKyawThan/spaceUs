import { useState } from "react";
import React from "react";
import {
  View,
  Text,
  Image,
  StyleSheet,
  TouchableOpacity,
  Icon,
} from "react-native";

const Post = ({ data }) => {
  const [isInterest, setIsInterest] = useState(data.love);
  const [isLove, setIsLove] = useState(data.interested);
  function reactClicked() {
    setIsLove(!isLove);
  }
  function interestClicked() {
    setIsInterest(!isInterest);
  }

  return (
    <View style={styles.container}>
      <View style={styles.userSection}>
        <Image source={{ uri: data.profile }} style={styles.profile} />
        <Text style={styles.username}>{data.username}</Text>
      </View>
      <View style={styles.content}>
        <Text> {data.content.caption} </Text>
        <Image
          source={{ uri: data.content.image }}
          style={styles.content.image}
        />
      </View>
      <View style={styles.reactions}>
        <Text
          style={[styles.reactions.react, isLove && styles.reactions.isLove]}
          onPress={reactClicked}
        >
          {isLove ? "Loved" : "Love"}
        </Text>
        <Text
          style={[styles.reactions.react, isInterest && styles.reactions.isLove]}
          onPress={interestClicked}
        >
            {isInterest ? "Interested": "Interest"}
        </Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginTop: 10,
    backgroundColor: "whitesmoke",
    width: "100%",
  },
  userSection: {
    flexDirection: "row",
    alignItems: "center",
  },
  profile: {
    width: 50,
    height: 50,
    backgroundColor: "grey",
    borderRadius: 50,
  },
  username: {
    fontWeight: "500",
    fontSize: 16,
    color: "darkgreen",
    alignItems: "center",
    paddingLeft: 10,
  },
  content: {
    flex: 1,
    marginTop: 10,
    flexDirection: "column",
    image: {
      height: 300,
    },
  },
  reactions: {
    height: 40,
    flex: 1,
    flexWrap: "wrap",
    flexDirection: "row",
    alignItems: "center",
    react: {
      width: "50%",
      textAlign: "center",
      height: "100%",
      // borderRadius: 20,
      padding: 10,
      backgroundColor: "lightblue",
    },
    isLove: {
      backgroundColor: "skyblue",
      width: "50%",
      textAlign: "center",
      height: "100%",
      // borderRadius: 20,
      padding: 10,
    },
  },
});

export default Post;
