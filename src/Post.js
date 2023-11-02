import React from "react";
import { View, Text, Image, StyleSheet } from 'react-native';

const Post = ({ data })=>{
    return (
        <View style={ styles.container }>
            <View style={ styles.userSection }>
                <Image source={{ uri: data.profile }} style={ styles.profile }/>
                <Text style={ styles.username }>{ data.username }</Text>
            </View>
            <View style={ styles.content }>
                <Text> { data.content.caption } </Text>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        marginTop: 10,
        backgroundColor: "whitesmoke",
        maxHeight: 100,
        width: "100%",
        overflow: "hidden"
    },
    userSection: {
        flexDirection: "row",
        alignItems: "center"
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
        color: "skyblue",
        alignItems: "center",
        paddingLeft: 10,
    },
    content: {
        marginTop: 10,
    }
})

export default Post;